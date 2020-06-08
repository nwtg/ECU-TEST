import textwrap

import numpy

if any(name not in globals() for name
        in ('NumpyBasedTraceStep', 'SignalDefinition', 'ParameterDefinition')):
    from NumpyBasedTraceStep import NumpyBasedTraceStep, SignalDefinition, ParameterDefinition


class CalculateDownsampledSignal_Average(NumpyBasedTraceStep):

    """
    This is an implementation of NumpyBasedTraceStep.

    Use the interface as reference for available methods. Abstract methods have to be implemented.
    Other methods like GetDescription() are optionally overwritten. There are utility functions
    like CalculateRanges(), FitToAxis() that can be used in your code.
    """

    @staticmethod
    def GetInterfaceRevision():
        """
        Returns the interface revision of the trace step template.

        :note: This method is auto-generated for new implementations of NumpyBasedTraceStep. So do
               not delete or modify this method!

        :rtype: int
        """
        return 1

    @classmethod
    def GetDescription(cls):
        """
        Returns the description of the trace step.

        :rtype: str
        """
        return textwrap.dedent('''
            This trace step template generates a down sampled signal.

            The down sampled signal gets only samples, when the value of the input signal changes or the "maxTimeBetweenSamples" is exceeded.
            ''').strip()

    @classmethod
    def GetSignals(cls):
        """
        Returns the incoming and outgoing signals of the trace step.

        :rtype: list[SignalDefinition]
        """
        return [
            SignalDefinition('Signal', 'IN', optional=False,
                             description='The signal that should be downsampled.'),
            SignalDefinition('DownsampledSignal', 'OUT', optional=False,
                             description='Downsampled signal of the input signal.'),
            ]

    @classmethod
    def GetParameters(cls):
        """
        Returns the input and return parameters of the trace step.

        :rtype: list[ParameterDefinition]
        """
        return [
            ParameterDefinition('maxTimeBetweenSamples', 'IN', default=0.1,
                                description=textwrap.dedent('''
                                    Maximum time between two samples for the signal.
                                    The time must be greater than zero.
                                    The unit is based on the trace file (mostly in seconds).

                                    None ... maxTimeBetweenSamples = 0.1s [Default]
                                    ''').strip())
            ]

    @classmethod
    def GetTimeAxisDefinition(cls):
        """
        Returns how the common time axis is determined. Only the logical operators **and** and
        **or** as well as references to the time axes of the signals by using the signal name are
        permitted. The use of brackets is allowed.

        :note: If a signal is not defined on the common time axis, its value is determined
               according to its interpolation rule.

        :return: Convention for building the common time axis (e.g. **'Sig1 or Sig2'**). If an
                 empty string is returned, all time axes are merged into one common time axis.
                 This corresponds to an OR concatenation of the individual time axes.
        :rtype: str
        """
        # e.g. 'Sig1 or Sig2' - timestamps either from Sig1 or Sig2 (default behavior)
        # e.g. 'Sig1 and Sig2' - only timestamps common to both Sig1 and Sig2
        return ''

    def Check(self, parameters):
        """
        Is called initially before trace analysis execution and should check the parameterization.
        In case of error, raise a TypeError or ValueError.

        :param parameters: Dictionary of parameter values.
        :type parameters: dict[str, object]
        :raise TypeError: Invalid type of a parameter.
        :raise ValueError: Invalid value of a parameter.
        """
        if not isinstance(parameters['maxTimeBetweenSamples'], (int, float)):
            raise TypeError(
                "The parameter 'maxTimeBetweenSamples' has no valid type ({}).".format(
                                                        type(parameters['maxTimeBetweenSamples'])))

        if parameters['maxTimeBetweenSamples'] <= 0:
            raise ValueError(
                "The parameter 'maxTimeBetweenSamples' must be greater then zero ({}).".format(
                                                        parameters['maxTimeBetweenSamples']))

    def Process(self, parameters, report, timeAxis, ranges, signals):
        """
        Method for executing the trace step template. Calculations can be performed based on
        the given signal values and their results can be stored in outgoing signals. Evaluation
        results and return parameters can be set.

        :note: It is recommended to evaluate over the given trigger ranges and set the result for
               each trigger range. The overall result will be automatically determined.

               It is possible to manually set the overall result using the :class:`Report` object;
               the automatic mechanism will be deactivated if used.

               Detailed spots are also reported on trigger ranges.
        :note: Access to values: All signal values within a trigger range can be accessed
               by its :class:`TriggerRange` object. Alternatively, all values of a signal can be
               accessed by the :class:`Signal` object.
        :note: To store calculated values in an outgoing signal the :class:`Signal` object is used:
               Signal.Emit(timestamps, values)
        :param parameters: Dictionary of parameter values.
        :type parameters: dict[str, object]
        :param report: The report object.
        :type report: :class:`Report`
        :param timeAxis: The common time axis of the signals over the entire trace. A limitation
                         to the trigger ranges can be provided by a :class:`TriggerRange` object.
        :type timeAxis: numpy.ndarray
        :param ranges: List of trigger ranges.
        :type ranges: list[TriggerRange]
        :param signals: Dictionary of signals.
        :type signals: dict[str, :class:`Signal`]
        """
        for triggerRange in ranges:
            timesIn = triggerRange.GetTimestamps()
            valuesIn = triggerRange.GetValues('Signal')
            sampleCount = len(timesIn)

            # empty signal
            if sampleCount == 0:
                triggerRange.SetResultText('Input signal is empty.')
                continue

            # output values and times maximum size
            timesOut = numpy.copy(timesIn)
            valuesOut = numpy.copy(valuesIn)

            j = 0
            k = 0
            valueSum = 0
            # calculate arithmetic mean value in this duration
            for i in range(0, timesIn.shape[0]):
                # if timestamp not far enough -> collect the values
                if round(timesIn[i] - timesOut[k], 11) < round(parameters['maxTimeBetweenSamples'], 11):
                    valueSum += valuesIn[i]
                    thenFlag = True
                else:
                    valuesOut[j] = valueSum/(i-k)
                    timesOut[j] = timesIn[k]
                    j += 1
                    k = i
                    valueSum = valuesIn[i]
                    thenFlag = False

            if thenFlag:
                valuesOut[j] = valueSum/(i-k+1)
                timesOut[j] = timesIn[k]
                triggerRange.SetResultText('The last sector is shorter than {duration}s'.format(duration=parameters['maxTimeBetweenSamples']))
                numSamples = j+1
            else:
                numSamples = j
            timesOut = numpy.resize(timesOut, numSamples)
            valuesOut = numpy.resize(valuesOut, numSamples)
            # emit output signal
            signals['DownsampledSignal'].Emit(timesOut, valuesOut)
