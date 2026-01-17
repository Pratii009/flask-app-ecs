@Library("Shared") _
pipeline{

    agent {label "vaibhav"}

    stages{
        stage("hello"){
            steps{
                script{
                    hello()
                }
            }
        }
        stage("code"){
            steps{
                script{
                    clone("https://github.com/Pratii009/flask-app-ecs.git","main")
                }
                // echo "cloning the code"
                // git url:"https://github.com/Pratii009/flask-app-ecs.git",branch:"main"
                // echo "clonned successfully"
        }
    }
         stage("build"){
            steps{
                script{
                    dockerbuild("flask-app-img","latest","pratiksha293")
                }
                // echo "building the code"
                // bat "docker build -t flask-app:latest ."
                // echo "image built successfully"
        }
    }
         stage("push to dockerhub"){
            steps{
                
                script{
                    dockerpush("flask-app-img","latest","pratiksha293")
                }
                // echo "testing the code"
                // withCredentials([usernamePassword(credentialsId:"dockerhubcred",
                // passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
                // sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                // sh "docker image tag flask-app:latest ${env.dockerHubUser}/flask-app:latest"
                // sh "docker push ${env.dockerHubUser}/flask-app:latest "
                
              }
        }
         stage("deploy"){
            steps{
                echo "deploying the code"
                sh "docker stop flask-app || true"
                sh "docker rm flask-app || true"
                sh "docker run -d -p 80:80 flask-app:latest"
                echo "deployed successfully"
             }
          }
 }
}
