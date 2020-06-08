import os
import sys
import winreg

reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\TraceTronic\ECU-TEST 8.1')
etDir = winreg.QueryValueEx(reg, 'Path')[0]
reg.Close()
ApiClientPath = os.path.join(etDir, r'Templates\ApiClient')
sys.path.append(ApiClientPath)

from ApiClient import ApiClient

api = ApiClient()

def createTA(pkgFile, trcp_path, blockName='CalculateAverage'):
    pkg = api.PackageApi.OpenPackage(pkgFile)
    # check if there is already trace analysis exists, if not, create one new.
    if pkg.GetTraceAnalyses():
        ta = pkg.GetTraceAnalyses()[0]
    else:
        ta = api.PackageApi.TraceAnalysisApi.CreateTraceAnalysis(blockName)
        pkg.AppendTraceAnalysis(ta)
    # check if there is already "Episode" steps exist, if not, create one new.
    if ta.GetTraceSteps()[-1].GetType() == 'Episode':
        episode = ta.GetTraceSteps()[-1]
    else:
        episode = api.PackageApi.TraceAnalysisApi.CreateEpisode(blockName)
        ta.AppendTraceStep(episode)
    # create one analysis block
    anaBlock = api.PackageApi.TraceAnalysisApi.CreateBlock(blockName)
    episode.AppendTraceStep(anaBlock)
    # create one recording step
    recordingStep = api.PackageApi.TraceAnalysisApi.CreateSignalRecording(blockName)
    # create signal connections from signal recording groups, and create TRCP steps.
    signalGroups = pkg.GetSignalGroups()
    for signalGroup in signalGroups:
        recordingGroup = signalGroup.GetRecordingGroups()[0]
        mappingItemNames = signalGroup.GetMappingItemNames()
        for mappingItemName in mappingItemNames:
            # process generic signal names to satisfy name rules of python identifiers.
            genericSignalName_Trace = mappingItemName.replace(' ', '').replace('/', '_').replace('[', '').replace(']', '').replace('%','').replace('|','_')
            genericSignal = api.PackageApi.TraceAnalysisApi.CreateGenericSignal(genericSignalName_Trace)
            ta.AppendGenericSignal(genericSignal)
            genericSignal.AssignRecordingSignal(recordingGroup, mappingItemName)
            # create out signals in advance.
            outSignal = api.PackageApi.TraceAnalysisApi.CreateGenericSignal(genericSignalName_Trace+'_avg')
            ta.AppendGenericSignal(outSignal)
            # create templated trace step.
            trcp_average = api.PackageApi.TraceAnalysisApi.CreateTemplateBasedTraceStep(blockName)
            # TODO: can use search mode
            trcp_average.SetTemplateById(trcp_path)
            trcp_average.SetParameters({'maxTimeBetweenSamples': '1'})
            anaBlock.AppendTraceStep(trcp_average)
            trcp_average.AssignGenericSignalByName('Signal', genericSignalName_Trace)
            trcp_average.AssignGenericSignalByName('DownsampledSignal', genericSignalName_Trace+'_avg')
            # append signal to recording step.
            recordingStep.AddGenericSignalByName(genericSignalName_Trace+'_avg')

    recordingStep.SetStoreType('CSV')
    recordingStep.SetFileExpression(repr(blockName))
    anaBlock.AppendTraceStep(recordingStep)
    pkg.Save()


if __name__ == '__main__':
    createTA(r'\\Mac\Home\Desktop\OneDrive\3_ET_Workspaces\9_2019test_ET8.1\Packages\test_toto\testNumpyAverage_2.pkg', 
             r'Ricardo\CalculateDownsampledSignal_Average')