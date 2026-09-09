pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t fastapi-k8s-demo:v1 .'
            }
        }
    }
}
