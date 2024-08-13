pipeline {
    agent {
        label 'kubernetes-agent' 
    }
    environment {
        // Docker Hub credentials, GitHub credentials, and kubeconfig file for K3s
        DOCKERHUB_CREDENTIALS = credentials('DockerHub') 
        GIT_CREDENTIALS = credentials('GitHub') 
        KUBECONFIG_CREDENTIALS = credentials('k3s') 
        DOCKER_IMAGE = "iliqpetrov/simple_app:latest" 
        GIT_REPO = "https://github.com/iipetrov/Sre_Task.git"
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Starting code checkout from GitHub...'
                // Checking out the code from GitHub
                git branch: 'main', credentialsId: 'GitHub', url: "${GIT_REPO}"
                echo 'Code checkout completed.'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Starting Docker build...'
                    // Building the Docker image
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                    echo 'Docker build completed.'
                }
            }
        }
        stage('Deploy to K3s for Testing') {
            steps {
                script {
                    echo 'Deploying to K3s for testing...'
                    // Applying Kubernetes deployment for testing
                    sh '''
                    echo "${KUBECONFIG_CREDENTIALS}" > kubeconfig
                    export KUBECONFIG=kubeconfig
                    kubectl apply -f deployment.yaml
                    '''
                    echo 'Deployment to K3s completed.'
                }
            }
        }
        stage('Run Automated Tests') {
            steps {
                echo 'Running automated tests...'
                // Running unit tests
                script {
                    sh 'python -m unittest discover -s tests'
                }
                echo 'Automated tests completed.'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    echo 'Pushing Docker image to Docker Hub...'
                    // Pushing the Docker image to Docker Hub
                    docker.withRegistry('', 'DockerHub') {
                        sh 'docker push ${DOCKER_IMAGE}'
                    }
                    echo 'Docker image pushed to Docker Hub.'
                }
            }
        }
        stage('Deploy to Production') {
            steps {
                script {
                    echo 'Deploying Docker image to production...'
                    // Deploying the Docker image to production
                    sh '''
                    echo "${KUBECONFIG_CREDENTIALS}" > kubeconfig
                    export KUBECONFIG=kubeconfig
                    kubectl set image deployment/myapp myapp=${DOCKER_IMAGE} --record
                    '''
                    echo 'Deployment to production completed.'
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
