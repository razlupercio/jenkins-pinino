pipeline{
    agent any
    parameters {
        choice(
            name: 'Env',
            choices: 'dev\nqa\nuat\nprod',
            description: 'passing the env'
            )
    }
    stages {
        stage('Environment'){
            steps {
                echo "The env is ${params.Env}"
            }
        }
    }
}
