pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Compile') {
            steps {
                sh 'python3 -m compileall -q .'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --user pytest flask requests'
            }
        }

        stage('Start API') {
            steps {
                sh 'python3 stand_up_triangle_api.py > api.log 2>&1 &'
                sh 'sleep 3'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }

    post {
        always {
            sh '''
                PIDS=$(ps -ef | grep "stand_up_triangle_api.py" | grep -v grep | awk '{print $2}')

                if [ -n "$PIDS" ]; then
                    echo "Stopping API process(es): $PIDS"
                    kill $PIDS
                else
                    echo "No API process found"
                fi
            '''

            archiveArtifacts artifacts: 'api.log', allowEmptyArchive: true
        }

        success {
            echo 'All tests passed successfully.'
        }

        failure {
            echo 'The build failed. Review the console output for details.'
        }
    }
}
