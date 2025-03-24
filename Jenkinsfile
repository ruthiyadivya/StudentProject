pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "your-dockerhub-username/studentproject"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/studentproject.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        
        stage('Login to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'docker-hub-password', variable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u your-dockerhub-username --password-stdin'
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }
    }
}
