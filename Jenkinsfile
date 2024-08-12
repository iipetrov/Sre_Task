pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('3033') // Replace with your Docker Hub credentials ID
        KUBE_CONFIG = credentials('0b8fffb2-bc5c-4200-aced-59e7405341ce	') // Replace with your Kubernetes credentials ID
        DOCKER_IMAGE = "iliyapetrov/simple-web-app:${env.BUILD_NUMBER}" // Replace with your Docker Hub username
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    credentialsId: 'github-credentials-id', // Replace with your GitHub SSH credentials ID
                    url: 'https://github.com/iipetrov/Sre_Task.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Test Container') {
            steps {
                script {
                    sh 'docker run --rm ${DOCKER_IMAGE} python --version' // Example test step
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_HUB_CREDENTIALS) {
                        sh 'docker push ${DOCKER_IMAGE}'
                    }
                }
            }
        }

        stage('Deploy to K3s') {
            steps {
                script {
                    withKubeConfig([credentialsId: KUBE_CONFIG, namespace: 'default']) {
                        sh """
                        kubectl set image deployment/simple-web-app simple-web-app=${DOCKER_IMAGE}
                        kubectl rollout status deployment/simple-web-app
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment succeeded!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
