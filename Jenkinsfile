pipeline{
    agent any

    environment{
        PYTHON_SCRIPT_PATH = 'fetch_teams.py'
    }

    parameters {
        choice(
            name: 'TEAM',
            choices: getTeam(),
            description: 'Select the team'
            )
    }

    stages {
        stage('Fetch Teams'){
            steps {
                script {
                    echo "Selected Team: ${params.TEAM}"
                }
            }
        }
    }
}

// function to fetch teams 

def getTeams() {
    node {
        def teamsJson = sh(script: "python3 ${env.PYTHON_SCRIPT_PATH}", returnStdout: true).trim()
        def teams = readJSON(text: teamsJson)
        return teams
    }
}
