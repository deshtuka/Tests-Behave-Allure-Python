pipeline {
    agent any
    parameters {
        gitParameter (  branch: '',
                        branchFilter: 'origin/(.*)',
                        defaultValue: 'master',
                        description: '',
                        name: 'BRANCH',
                        quickFilterEnabled: true,
                        selectedValue: 'TOP',
                        sortMode: 'DESCENDING',
                        tagFilter: '*',
                        type: 'PT_BRANCH',
                        useRepository: 'https://github.com/deshtuka/Tests-Behave-Allure-Python.git')
    }

    stages {
        stage('Cloning Git') {
            steps {
                deleteDir()
                git branch: "${params.BRANCH}", url: 'https://github.com/deshtuka/Tests-Behave-Allure-Python.git'
            }
        }
        stage('Build') {
        	steps {
        		sh """
        			python3 --version
        			python3 -m venv .venv
        			. .venv/bin/activate
        			pip3 install -r requirements.txt
        			pip3 list
        		"""
        	}
        }
        stage('Test') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh """
                        . .venv/bin/activate
                        /var/jenkins_home/.local/bin/behave -f allure_behave.formatter:AllureFormatter -o allure_result_folder --tags=${TAGS}"""
                }
            }
        }
        stage('Reports') {
            steps {
                allure([
                includeProperties: false,
                jdk              : '',
                properties       : [],
                reportBuildPolicy: 'ALWAYS',
                results          : [[path: 'allure_result_folder']]
                ])
            }
        }
    }
}