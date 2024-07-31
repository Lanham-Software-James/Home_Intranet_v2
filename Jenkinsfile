pipeline {
    agent {
        label 'jenkins_agent'
    }

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
                sh "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} ."
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
        // stage('Create .env File') {
        //     steps {
        //         script {
        //             withCredentials([string(credentialsId: 'DEBUG', variable: 'DEBUG'), string(credentialsId: 'SECRET_KEY', variable: 'SECRET_KEY')]) {
                       
        //                 def fileContent = """
        //                     DEBUG=${DEBUG}
        //                     SECRET_KEY=${SECRET_KEY}
        //                 """

        //                 writeFile file: '.env', text: fileContent
        //             }
        //         }
        //     }
        // }
        // stage('Deploy') {
        //     steps {
        //         sshagent (credentials: ['pi-server-ssh-credentials']) {
        //             sh  """
        //                 scp -o StrictHostKeyChecking=no docker-compose ${credentials(REMOTE_HOST)}:/opt/stacks/intranet
                        
        //                 cd /opt/stacks/intranet
        //                 docker compose down
        //                 docker compose up

        //                 """
        //         }
        //     }
        // }
    }
}