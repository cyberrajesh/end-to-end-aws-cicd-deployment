pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        AWS_ACCOUNT_ID = '079379901810'
        ECR_REPOSITORY = 'devops-demo-app'
        IMAGE_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPOSITORY}"
        CONTAINER_NAME = 'devops-app'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies and Test') {
            steps {
                sh '''
                    if [ -f application/app.py ]; then
                        APP_DIR=application
                    else
                        APP_DIR=.
                    fi

                    python3 -m pip install --user -r $APP_DIR/requirements.txt
                    python3 -m pip install --user pytest

                    if [ -d "$APP_DIR/tests" ]; then
                        python3 -m pytest "$APP_DIR/tests" -v
                    else
                        python3 -m py_compile $APP_DIR/app.py
                    fi
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t $ECR_REPOSITORY:$BUILD_NUMBER .
                    docker tag $ECR_REPOSITORY:$BUILD_NUMBER $IMAGE_URI:$BUILD_NUMBER
                    docker tag $ECR_REPOSITORY:$BUILD_NUMBER $IMAGE_URI:latest
                '''
            }
        }

        stage('Push to Amazon ECR') {
            steps {
                sh '''
                    aws ecr get-login-password --region $AWS_REGION | \
                    docker login --username AWS --password-stdin $IMAGE_URI

                    docker push $IMAGE_URI:$BUILD_NUMBER
                    docker push $IMAGE_URI:latest
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true

                    docker run -d \
                    --name $CONTAINER_NAME \
                    -p 80:5000 \
                    $IMAGE_URI:$BUILD_NUMBER
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    for i in $(seq 1 10); do
                        if curl -fsS http://localhost/health; then
                            echo "Application is healthy!"
                            exit 0
                        fi
                        sleep 5
                    done

                    echo "Health check failed!"
                    exit 1
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed. Check Console Output.'
        }
    }
}
