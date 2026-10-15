
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    triggers {
        githubPush()
    }

    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cloud-app:latest .'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker run --rm cloud-app:latest python -c \
                    "from app import app; assert app.test_client().get('/').status_code == 200"
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f cloud-app || true

                    docker run -d \
                      --name cloud-app \
                      --restart unless-stopped \
                      -p 5000:5000 \
                      cloud-app:latest

                    sleep 3
                    docker ps --filter name=cloud-app
                    curl --fail http://localhost:5000/
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the stage console output.'
        }
    }
}
