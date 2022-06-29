// Jenkinsfile

pipeline {
    agent {
        label 'firestorm'
    }
    
    stages {
        stage('build') {
            steps {
                withCredentials([string(credentialsId: 'archer-a9-router-web-password', variable: 'ARCHER_A9_ROUTER_WEB_PASSWORD')]) {
                    sh 'docker build -t archer-a9-uptime --build-arg router_password=$ARCHER_A9_ROUTER_WEB_PASSWORD .'
                }
                
                sh 'test -d /var/log/archer-a9-uptime || sudo rm -rf /var/log/archer-a9-uptime && sudo mkdir -p /var/log/archer-a9-uptime'
            }
        }
        
        stage('test') {
            steps {
                echo 'Run tests here'
            }
        }
        
        stage('deploy') {
            steps {
                echo 'Deploy here'
                sh 'docker run --network=host -v /var/log/archer-a9-uptime:/data --name archer-a9-uptime --rm archer-a9-uptime'
            }
        }
    }
    
    post {
        regression {
            withCredentials([string(credentialsId: 'ifttt-push-notification-webhook', variable: 'IFTTT_PUSH_NOTIFICATION_WEBHOOK')]) {
                sh 'curl -X POST -H \'Content-Type: application/json\' -d \'{"value1": "Build Broke", "value2": "Jenkins build for archer-a9-uptime has failed"}\' $IFTTT_PUSH_NOTIFICATION_WEBHOOK'
            }
        }
        
        fixed {
            withCredentials([string(credentialsId: 'ifttt-push-notification-webhook', variable: 'IFTTT_PUSH_NOTIFICATION_WEBHOOK')]) {
                sh 'curl -X POST -H \'Content-Type: application/json\' -d \'{"value1": "Build Fixed", "value2": "Jenkins build for archer-a9-uptime was successful"}\' $IFTTT_PUSH_NOTIFICATION_WEBHOOK'
            }
        }
        
        cleanup {
            cleanWs()
        }
    }
}
