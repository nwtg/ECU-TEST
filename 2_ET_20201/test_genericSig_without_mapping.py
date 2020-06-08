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

pkg = api.PackageApi.OpenPackage(r'\\Mac\Home\Desktop\OneDrive\3_ET_Workspaces\9_2019test_ET8.1\Packages\test_toto\test_genericSignal_without_mapping.pkg')
ta = pkg.GetTraceAnalyses()[0]
sigBindings = {}
genericSignals = ta.GetGenericSignals()
for genSig in genericSignals:
    
    sigBindings[genSig.GetAssignedMappingItemName()] = genSig.GetName()

print(sigBindings)