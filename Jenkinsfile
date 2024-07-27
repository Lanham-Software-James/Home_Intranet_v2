pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "jameslanham/home-intranet-v2"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Unit Tests') {
            steps {
                echo 'Running Unit Tests..'
            }
        }
        stage('Build Image') {
            steps {
                sh "docker build --platform linux/amd64 -t ${DOCKER_IMAGE}:${IMAGE_TAG} ."
                sh "docker tag ${DOCKER_IMAGE}:${IMAGE_TAG} ${DOCKER_IMAGE}:latest"
            }
        }
        stage('Image Tests') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'DOCKERHUB_PASSWORD', usernameVariable: 'DOCKERHUB_USERNAME')]) {
                        sh "echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin"
                    }
                }
            }
        }
        stage('Push Image') {
            steps {
                sh "docker push ${DOCKER_IMAGE}:${IMAGE_TAG}"
                sh "docker push ${DOCKER_IMAGE}:latest"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}