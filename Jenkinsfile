pipeline {
    agent {
        label 'kubernetes-agent' 
    }
    environment {
        DOCKERHUB_CREDENTIALS = credentials('DockerHub') 
        GIT_CREDENTIALS = credentials('GitHub') 
        KUBECONFIG_CREDENTIALS = credentials('k3s') 
        DOCKER_IMAGE = "iliqpetrov/simple_app:latest" 
        GIT_REPO = "https://github.com/iipetrov/Sre_Task.git"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'GitHub', url: "${GIT_REPO}"
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }
        stage('Deploy to K3s for Testing') {
            steps {
                script {
                    sh '''
                    echo "${KUBECONFIG_CREDENTIALS}" > kubeconfig
                    export KUBECONFIG=kubeconfig
                    kubectl apply -f deployment.yaml
                    '''
                }
            }
        }
        stage('Run Automated Tests') {
            steps {
                // Заменете с вашите тестове
                script {
                    sh 'python -m unittest discover -s tests'
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', 'DockerHub') {
                        sh 'docker push ${DOCKER_IMAGE}'
                    }
                }
            }
        }
        stage('Deploy to Production') {
            steps {
                script {
                    sh '''
                    echo "${KUBECONFIG_CREDENTIALS}" > kubeconfig
                    export KUBECONFIG=kubeconfig
                    kubectl set image deployment/myapp myapp=${DOCKER_IMAGE} --record
                    '''
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
