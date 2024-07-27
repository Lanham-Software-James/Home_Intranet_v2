pipeline {
    agent any

    stages {
        stage('Unit Tests') {
            steps {
                echo 'Running Unit Tests..'
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t home-intranet-v2:latest .'
            }
        }
        stage('Image Tests') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Push Image') {
            steps {
                echo 'Pushing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}