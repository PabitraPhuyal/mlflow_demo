pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/<PabitraPhuyal>/mlops-demo.git'
            }
        }

        stage('Train Model + MLflow Logging') {
            steps {
                sh 'python src/train.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t mlops-demo:latest .'
            }
        }

        stage('Push to Registry') {
            steps {
                sh 'docker tag mlops-demo:latest <your-dockerhub>/mlops-demo:latest'
                sh 'docker push <your-dockerhub>/mlops-demo:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s-deployment.yaml'
            }
        }
    }
}