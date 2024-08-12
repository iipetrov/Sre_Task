pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials-id') // Replace with your Docker Hub credentials ID
        DOCKER_IMAGE = "<твоето-потребителско-име>/simple-web-app:${env.BUILD_NUMBER}"
        KUBE_CONFIG = credentials('kube-config') // Replace with your Kubernetes credentials ID
    }

    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo/simple-web-app.git' // Replace with your GitHub repo URL
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
