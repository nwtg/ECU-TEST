import requests
import json
import os
import sys
import argparse
import time
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('wsname')
args = parser.parse_args()
params = vars(args)

def getJenkinsNode(ip, authKey, projectId, wbmap, wsname, bnmap):
    getResourceUrl = 'http://{ip}:8085/api/v2/monitoring/resources'.format(ip=ip)
    getBenchStatus = 'http://{ip}:8085/api/v2/monitoring/testexecution'.format(ip=ip)
    getBenchHeartBeat = 'http://{ip}:8085/api/v2/monitoring/heartbeat'.format(ip=ip)
    params = {'projectId':projectId, 'authKey':authKey}
    benches = requests.get(getResourceUrl, params).json()
    avaBenches = loadJson(wbmap)[0][wsname]
    exeProgressDict = {}
    for bench in avaBenches:
        for b in benches:
            if bench in b.values():
                resourceId = benches[benches.index(b)] # type: Dict
        params.update(resourceId)
        online = requests.get(getBenchHeartBeat, params).json()['online']
        if online:
            exeInfo = requests.get(getBenchStatus, params).json()
            benchStatus = exeInfo['status']
            if benchStatus == 'IDLE':
                nodeLabel = loadJson(bnmap)[0][bench]
                return nodeLabel
            else:
                exeProgress = exeInfo['actual']/exeInfo['total']
                exeProgressDict[bench] = exeProgress
            
    idlestBench = list(exeProgressDict.keys())[list(exeProgressDict.values()).index(min(exeProgressDict.values()))]
    nodeLabel = loadJson(bnmap)[0][idlestBench]
    return nodeLabel

def loadJson(jsonPath):
    with open(jsonPath, 'r') as f:
        jsonContent = f.read()
    text = json.loads(jsonContent)
    return text

ip = '10.211.55.2'
bench_node = 'bench_node_mapping.json'
ws_bench = 'ws_bench_mapping.json'
authKey = 'SPsdDWt2WinZ1iZBN9Sb4ehCZe41qZkLJV7uKiBiBhLwS6kOuivdxkbLbAiRIOwrPr_pxnetu0GqK4LagJc8hq-MvraD7YWG9D971fR-X0QxIy7ldwayRl8-CYGEnK7kVKUw4PF3QAWwhFjiN26Khs-RqGuWickjnPFgswXsowFSiBhcPGpEIU10wHG0HdBLtrK_W0noOseSNM2WBeqTA6KZKYfIjab06v5DZJ-rKZRjJU0EMhhP2WhkEPVxPUZeeM7ZPXuFa_1YG9QbfQVGe86EU2eDIrZcfWIaCZrhiZMY_To3O6Zrj2AHHfNBh5yyQRi33V_KNsp2R_fy7qjte6FzXFUoSNHki57XoeXEiq0rZsYunUtvjkZu6hz78bz0f86RxvNlV6K9GKCHnduGGQ=='
projectId = '1'
wsname = params['wsname']


idlestBench = getJenkinsNode(ip, authKey, projectId, ws_bench, wsname, bench_node)
with open(r'jenkinsNode.properties', 'w') as f:
    f.write('env.jenkinsNode={}'.format(repr(idlestBench)))
# print(idlestBench)