pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('3003') 
        DOCKER_IMAGE = "iliyapetrov/simple-web-app:${env.BUILD_NUMBER}"
        KUBE_CONFIG = credentials('502') 
    }

    stages {
        stage('Clone repository') {
            steps {
                git url: 'https://github.com/iipetrov/Sre_Task.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Test Container') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).inside {
                        sh 'python simple_app.py & sleep 5'
                        sh 'curl http://localhost:5000'
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_HUB_CREDENTIALS) {
                        docker.image(DOCKER_IMAGE).push()
                    }
                }
            }
        }

        stage('Deploy to K3s') {
            steps {
                script {
                    withKubeConfig([credentialsId: 'kube-config']) {
                        sh """
                        kubectl set image deployment/simple-web-app simple-web-app=${DOCKER_IMAGE} --namespace=default
                        kubectl rollout status deployment/simple-web-app --namespace=default
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
