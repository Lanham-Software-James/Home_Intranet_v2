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

        stage('Create .env File') {
            steps {
                script {
                    withCredentials([   string(credentialsId: 'DEBUG', variable: 'DEBUG'), 
                                        string(credentialsId: 'SECRET_KEY', variable: 'SECRET_KEY'), 
                                        string(credentialsId: 'POSTGRES_DB', variable: 'POSTGRES_DB'), 
                                        string(credentialsId: 'POSTGRES_USER', variable: 'POSTGRES_USER'), 
                                        string(credentialsId: 'POSTGRES_PASSWORD', variable: 'POSTGRES_PASSWORD')]) {
                       
                        def fileContent = "DEBUG=${DEBUG}\nSECRET_KEY=${SECRET_KEY}\nPOSTGRES_DB=${POSTGRES_DB}\nPOSTGRES_USER=${POSTGRES_USER}\nPOSTGRES_PASSWORD=${POSTGRES_PASSWORD}"

                        writeFile file: '.env', text: fileContent
                    }
                }
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

        stage('Prune Images') {
            steps {
                sh "docker image prune -af"
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'pi-server-ssh-credentials', passwordVariable: 'password', usernameVariable: 'user'), string(credentialsId: 'REMOTE_HOST', variable: 'host')]) {
                        def remote = [:]
                        remote.name = host
                        remote.host = host
                        remote.user = user
                        remote.password = password
                        remote.allowAnyHosts = true

                        sshCommand remote: remote, command: "cd /opt/stacks/intranet"
                        try {
                            sshCommand remote: remote, command: "docker compose down"
                        } catch (Exception e) {
                            echo "Failed to execute docker-compose down: ${e.getMessage()}"
                            throw e
                        }
                        sshCommand remote: remote, command: "rm -rf docker-compose.yml"
                        sshPut remote: remote, from: 'docker-compose.prod.yml', into: './docker-compose.yml'
                        sshCommand remote: remote, command: "docker compose up -d"
                    }
                }
            }
        }
    }
}