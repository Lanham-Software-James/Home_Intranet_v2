pipeline {
    agent any

    environment {
        DOCKER_IMAGE_DJANGO = "jameslanham/home-intranet-v2-django"
        DOCKER_IMAGE_NGINX = "jameslanham/home-intranet-v2-nginx"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        // Todo
        stage('Unit Tests') {
            steps {
                echo 'Running Unit Tests..'
            }
        }

        stage('Build Django Image') {
            steps {
                sh "docker build -f Dockerfile.Django -t ${DOCKER_IMAGE_DJANGO}:${IMAGE_TAG} ."
                sh "docker tag ${DOCKER_IMAGE_DJANGO}:${IMAGE_TAG} ${DOCKER_IMAGE_DJANGO}:latest"
            }
        }

        stage('Build Nginx Image') {
            steps {
                sh "docker build -f Dockerfile.Nginx -t ${DOCKER_IMAGE_NGINX}:${IMAGE_TAG} ."
                sh "docker tag ${DOCKER_IMAGE_NGINX}:${IMAGE_TAG} ${DOCKER_IMAGE_NGINX}:latest"
            }
        }

        // Todo
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

        stage('Push Django Image') {
            steps {
                sh "docker push ${DOCKER_IMAGE_DJANGO}:${IMAGE_TAG}"
                sh "docker push ${DOCKER_IMAGE_DJANGO}:latest"
            }
        }

        stage('Push Nginx Image') {
            steps {
                sh "docker push ${DOCKER_IMAGE_NGINX}:${IMAGE_TAG}"
                sh "docker push ${DOCKER_IMAGE_NGINX}:latest"
            }
        }
    }
}