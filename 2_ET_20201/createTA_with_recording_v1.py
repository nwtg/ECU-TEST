import os
import sys

def createTA(duration, api, pkgFile, trcp_path, blockName='CalculateAverage'):
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
        sigBindings = __GetGenericSignalNames(ta)
    else:
        ta = api.PackageApi.TraceAnalysisApi.CreateTraceAnalysis(blockName)
        pkg.AppendTraceAnalysis(ta)
        episode = api.PackageApi.TraceAnalysisApi.CreateEpisode(blockName)
        ta.AppendTraceStep(episode)
        sigBindings = {}

    # create one analysis block
    anaBlock = api.PackageApi.TraceAnalysisApi.CreateBlock(blockName)
    episode.AppendTraceStep(anaBlock)
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
            if mappingItemName in list(sigBindings.keys()):
                genericSignalName_Trace = sigBindings[mappingItemName]
            else:
                # if no generic signal created for this mapping item create one new.
                # process generic signal names to satisfy name rules of python identifiers.
                genericSignalName_Trace = mappingItemName.replace(' ', '_').replace('/', '_').replace('[', '_').replace(']', '_').replace('%','_').replace('|','_')
                genericSignal = api.PackageApi.TraceAnalysisApi.CreateGenericSignal(genericSignalName_Trace)
                ta.AppendGenericSignal(genericSignal)
                genericSignal.AssignRecordingSignal(recordingGroup, mappingItemName)

            outSignal_Name = genericSignalName_Trace+'_avg'
            # if outSignal_Name not in list(sigBindings.values()):
            if ta.GetGenericSignal(outSignal_Name) is None:
                outSignal = api.PackageApi.TraceAnalysisApi.CreateGenericSignal(outSignal_Name)
                ta.AppendGenericSignal(outSignal)
            # create templated trace step.
            trcp_average = api.PackageApi.TraceAnalysisApi.CreateTemplateBasedTraceStep(blockName)
            # TODO: can use search mode
            trcp_average.SetTemplateById(trcp_path)
            trcp_average.SetParameters({'duration': str(duration)})
            anaBlock.AppendTraceStep(trcp_average)
            trcp_average.AssignGenericSignalByName('Signal', genericSignalName_Trace)
            trcp_average.AssignGenericSignalByName('ArithmeticMean', outSignal_Name)
            # append signal to recording step.
            recordingStep.AddGenericSignalByName(outSignal_Name)

    recordingStep.SetStoreType('CSV')
    recordingStep.SetFileExpression(repr(blockName))
    anaBlock.AppendTraceStep(recordingStep)
    pkg.Save()

def __GetGenericSignalNames(ta):
    sigBindings ={}
    genericSignals = ta.GetGenericSignals()
    for genSig in genericSignals:
        sigBindings[genSig.GetAssignedMappingItemName()] = genSig.GetName()
    return sigBindings


if __name__ == '__main__':
    import winreg
    reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\TraceTronic\ECU-TEST 8.1')
    etDir = winreg.QueryValueEx(reg, 'Path')[0]
    reg.Close()
    ApiClientPath = os.path.join(etDir, r'Templates\ApiClient')
    sys.path.append(ApiClientPath)
    from ApiClient import ApiClient
    api = ApiClient()
    createTA(api, r'\\Mac\Home\Desktop\OneDrive\3_ET_Workspaces\9_2019test_ET8.1\Packages\test_toto\testNumpyAverage_2.pkg', 
             r'Ricardo\ArithmeticMean')