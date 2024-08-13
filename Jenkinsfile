pipeline {
    agent {
        kubernetes {
            label 'kubernetes-agent'
            yaml """
            apiVersion: v1
            kind: Pod
            spec:
              containers:
              - name: docker
                image: docker:latest
                command:
                - cat
                tty: true
                volumeMounts:
                - name: docker-socket
                  mountPath: /var/run/docker.sock
              - name: kubectl
                image: bitnami/kubectl:latest
                command:
                - cat
                tty: true
              volumes:
              - name: docker-socket
                hostPath:
                  path: /var/run/docker.sock
            """
        }
    }
    environment {
        DOCKERHUB_CREDENTIALS = credentials('DockerHub')
        GIT_CREDENTIALS = credentials('GitHub')
        KUBECONFIG_CREDENTIALS = credentials('k3s')
        DOCKER_IMAGE = "iliqpetrov/myapp:latest" // Заменете с вашето Docker Hub изображение
        GIT_REPO = "git@github.com:yourusername/yourrepo.git" // Заменете с вашето GitHub репо
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
                container('kubectl') {
                    script {
                        sh '''
                        echo "${KUBECONFIG_CREDENTIALS}" > kubeconfig
                        export KUBECONFIG=kubeconfig
                        kubectl apply -f deployment.yaml
                        '''
                    }
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
                container('kubectl') {
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
