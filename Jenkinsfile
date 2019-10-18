pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                dir ('lib') {
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                dir ('mongo_lib') {
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/mongo-lib.git"
                }
                dir ('mongo_lib/lib') {
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock==2.0.0 --user
                pip2 install pymongo==3.2.0 --user
                ./test/unit/mongo_rep_admin/chk_mem_rep_lag.py
                ./test/unit/mongo_rep_admin/chk_rep_lag.py
                ./test/unit/mongo_rep_admin/chk_rep_stat.py
                ./test/unit/mongo_rep_admin/fetch_members.py
                ./test/unit/mongo_rep_admin/fetch_priority.py
                ./test/unit/mongo_rep_admin/fetch_rep_lag.py
                ./test/unit/mongo_rep_admin/get_master.py
                ./test/unit/mongo_rep_admin/get_optimedate.py
                ./test/unit/mongo_rep_admin/help_message.py
                ./test/unit/mongo_rep_admin/main.py
                ./test/unit/mongo_rep_admin/process_json.py
                ./test/unit/mongo_rep_admin/prt_rep_stat.py
                ./test/unit/mongo_rep_admin/rep_health_chk.py
                ./test/unit/mongo_rep_admin/rep_msg_chk.py
                ./test/unit/mongo_rep_admin/rep_state_chk.py
                ./test/unit/mongo_rep_admin/run_program.py
                deactivate
                rm -rf test_env
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/sonarqube_code_coverage.sh'
                sh 'rm -rf lib'
                sh 'rm -rf mongo_lib'
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.JACIDM.properties"
                }
            
            }
        }
        stage('Artifactory upload') {
            steps {
                script {
                    server = Artifactory.server('Artifactory')
                    server.credentialsId = 'svc-highpoint-artifactory'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/mongo-rep-admin/"
                            },
                            {
                                "pattern": "./*.txt",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/mongo-rep-admin/"
                            },
                            {
                                "pattern": "./*.md",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/mongo-rep-admin/"
                            },
                            {
                                "pattern": "*.TEMPLATE",
                                "recursive": true,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/mongo-rep-admin/config/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
}
