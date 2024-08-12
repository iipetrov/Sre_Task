pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'docker-credentials-id'  // Вашите Docker Hub креденциали
        REGISTRY = 'docker.io'  // Може да се замени с вашия Docker хранилище
        IMAGE_NAME = 'flask-app'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                // Клонирайте кода от GitHub
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Изграждане на Docker образа
                    docker.build("${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Логнете се в Docker хранилището
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS_ID}") {
                        // Натоварете Docker образа
                        docker.image("${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}").push()
                    }
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                script {
                    // Деплойте приложението на Kubernetes
                    sh 'kubectl apply -f k8s/deployment.yaml'
                    sh 'kubectl apply -f k8s/service.yaml'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Стартирайте тестовете
                    sh 'curl -f http://flask-app-service:80/test'  // Примерен тест чрез HTTP заявка
                }
            }
        }

        stage('Deploy to Production') {
            when {
                expression { return currentBuild.result == 'SUCCESS' }
            }
            steps {
                script {
                    // Деплойте приложението на Kubernetes в продукционна среда
                    sh 'kubectl apply -f k8s/production-deployment.yaml'
                    sh 'kubectl apply -f k8s/production-service.yaml'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline успешно завършен.'
        }
        failure {
            echo 'Pipeline неуспешен.'
        }
    }
}
