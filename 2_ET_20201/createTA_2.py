
# function must be named 'func'

def func(duration, startTime, stopTime, api, pkgFile, trcp_path, blockName='CalculateAverage'):
    pkg = api.PackageApi.OpenPackage(pkgFile)
    # check if there is already trace analysis exists, if not, create one new.
    if pkg.GetTraceAnalyses():
        ta = pkg.GetTraceAnalyses()[0]
        # check if there is already "Episode" steps exist, if not, create one new.
        if ta.GetTraceSteps()[-1].GetType() == 'Episode':
            episode = ta.GetTraceSteps()[-1]
        else:
            episode = api.PackageApi.TraceAnalysisApi.CreateEpisode(blockName)
            ta.AppendTraceStep(episode)
    else:
        ta = api.PackageApi.TraceAnalysisApi.CreateTraceAnalysis(blockName)
        pkg.AppendTraceAnalysis(ta)
        episode = api.PackageApi.TraceAnalysisApi.CreateEpisode(blockName)
        ta.AppendTraceStep(episode)

    # create one trigger block
    triggerBlock = api.PackageApi.TraceAnalysisApi.CreateTriggerBlock(blockName)
    episode.AppendTraceStep(triggerBlock)
    # create one analysis block
    anaBlock = api.PackageApi.TraceAnalysisApi.CreateBlock(blockName)
    triggerBlock.AppendTraceStep(anaBlock)
    # create one recording step
    recordingStep = api.PackageApi.TraceAnalysisApi.CreateSignalRecording(blockName)
    # create signal connections from signal recording groups, and create TRCP steps.
    signalGroups = pkg.GetSignalGroups()
    for signalGroup in signalGroups:
        # Only first recording group of this signal group will be used.
        recordingGroup = signalGroup.GetRecordingGroups()[0]
        mappingItemNames = signalGroup.GetMappingItemNames()
        for mappingItemName in mappingItemNames:
            # check if this mapping item has been assigned to generic signal.
            # if no generic signal created for this mapping item create one new.
            # process generic signal names to satisfy name rules of python identifiers.
            genericSignalName_Trace = mappingItemName.replace(' ', '_').replace('/', '_').replace('[', '_').replace(']', '_').replace('%','_').replace('|','_').replace(':', '_')
            if ta.GetGenericSignal(genericSignalName_Trace) is None:
                genericSignal = api.PackageApi.TraceAnalysisApi.CreateGenericSignal(genericSignalName_Trace)
                ta.AppendGenericSignal(genericSignal)
                genericSignal.AssignRecordingSignal(recordingGroup, mappingItemName)
            else:
                print('Generic signal {} has already been created before, it will be used directly.'.format(genericSignalName_Trace))

            outSignal_Name = genericSignalName_Trace+'_avg'
            # if outSignal_Name not in list(sigBindings.values()):
            if ta.GetGenericSignal(outSignal_Name) is None:
                outSignal = api.PackageApi.TraceAnalysisApi.CreateGenericSignal(outSignal_Name)
                ta.AppendGenericSignal(outSignal)
            else:
                print('Generic signal {} has already been created before, it will be used directly.'.format(outSignal_Name))
            
            # create templated trace step.
            trcp_average = api.PackageApi.TraceAnalysisApi.CreateTemplateBasedTraceStep(blockName)
            # TODO: can use search mode
            trcp_average.SetTemplateById(trcp_path)
            trcp_average.SetParameters({'duration': str(duration), 'startTime': str(startTime)})
            anaBlock.AppendTraceStep(trcp_average)
            trcp_average.AssignGenericSignalByName('Signal', genericSignalName_Trace)
            trcp_average.AssignGenericSignalByName('ArithmeticMean', outSignal_Name)
            # append signal to recording step.
            recordingStep.AddGenericSignalByName(outSignal_Name)

    recordingStep.SetStoreType('CSV')
    recordingStep.SetFileExpression(repr(blockName))
    anaBlock.AppendTraceStep(recordingStep)
    triggerBlock.SetStartTrigger('{startTime} < Time() + {sigName}*0 < {stopTime}'.format(startTime=startTime, stopTime=stopTime, sigName=genericSignalName_Trace))
    triggerBlock.SetTriggerMode(triggerBlock.MODE_WHILE_STARTTRIGGER)
    pkg.Save()

