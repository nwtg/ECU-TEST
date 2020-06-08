pipeline {
   agent any
   stages {
      stage('getJenkinsNode') {
        agent {
            node {
                // any Windows node
                label 'ytspc'
            }
        }
         steps {
            // Echo
            bat label: '', script: '''cd C:\\Users\\Public\\Documents\\Jenkins_Home
                                      python .\\getJenkinsNode.py "1_Trex"'''
            script{
                load('C:/Users/Public/Documents/Jenkins_Home/jenkinsNode.properties')}
            echo "${env.jenkinsNode}"
         }
      }
      stage('Execute test project') {
        agent {
            node {
                label "${env.jenkinsNode}"
            }
        }
        steps {
            //Checkout
            checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'github_private', url: 'https://github.com/nwtg/ECU-TEST.git']]])
            
            // Start ET
            startET toolName: 'ECU-TEST', workspaceDir: '1_TRex'
            
            // Run project
            testProject testConfig: [constants: [], forceReload: false, keepConfig: false, loadOnly: false, tbcFile: '', tcfFile: 'CounterTimeout.tcf'], testFile: 'CounterTimeout\\CounterTimeoutDemo.prj'
            
            // Upload report to Jenkins
            publishUNIT 'ECU-TEST'
            
            // Upload ATX to TEST-GUIDE
            publishATX atxName: 'TEST-GUIDE', runOnFailed: true
            
            // Stop ECU-TEST
            stopET 'ECU-TEST'
        }
      }
   }
}