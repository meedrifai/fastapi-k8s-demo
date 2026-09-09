pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t meedrifai/fastapi-k8s-demo:v1 .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    bat 'docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%'
                    bat 'docker push meedrifai/fastapi-k8s-demo:v1'
                }
            }
        }
    }
}
