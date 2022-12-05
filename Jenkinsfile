pipeline {
    agent any
    stages {
        stage('Cloning Git') {
            steps {
                git 'https://github.com/deshtuka/Tests-Behave-Allure-Python.git'
            }
        }
        stage('Build') {
            steps {
                sh '''pip install virtualenv
                      python -m venv env
                      source env/bin/activate
                      pip install -r requirements.txt
                      deactivate'''
            }
        }
        stage('Test') {
            steps {
                sh '''source env/bin/activate
                      behave -f allure -o report ./features/api/api_test.feature'''
            }
        }
        stage('Reports') {
            steps {
                allure([
                includeProperties: true,
                jdk              : '',
                properties       : [],
                reportBuildPolicy: 'ALWAYS',
                results          : [[path: 'report']]
                ])
            }
        }
    }
}