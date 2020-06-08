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
            bat label: '', script: '''python .\\getJenkinsNode.py "2_ET_20201"'''
            script{
                load('jenkinsNode.properties')}
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
            //checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'github_private', url: 'https://github.com/nwtg/ECU-TEST.git']]])
            
            // Start ET
            startET toolName: 'ECU-TEST', workspaceDir: '2_ET_20201'
            
            // Run project
            testProject testConfig: [constants: [], forceReload: false, keepConfig: false, loadOnly: false, tbcFile: 'Presi\\SW_Ver_1_Testlab_HiL.tbc', tcfFile: 'Presi\\SW_Ver_1_Const.tcf'], testFile: 'Presi\\EV_TEST.prj'
            
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