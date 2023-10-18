'''
______             _              _            _                _              
| ___ \           (_)            | |          | |              | |             
| |_/ /_ __  ___   _   ___   ___ | |_     ___ | |_  __ _  _ __ | |_  ___  _ __ 
|  __/| '__|/ _ \ | | / _ \ / __|| __|   / __|| __|/ _` || '__|| __|/ _ \| '__|
| |   | |  | (_) || ||  __/| (__ | |_    \__ \| |_| (_| || |   | |_|  __/| |   
\_|   |_|   \___/ | | \___| \___| \__|   |___/ \__|\__,_||_|    \__|\___||_|   
                 _/ |                                                        
                |__/                                                By Minuta18                                                         

This is a script to make porject creation and development faster
'''

import sys

def print_help():
    print('''Usage: ProjectStarter <SUBCOMMAND> [OPTIONS]

This is a script to make porject creation and development faster. Uses PyProject.toml

Available subcommands:
    init                Create a new PyProject.toml and initialize the project in the current directory
    create <object>     Creates a new object (like service or application) in the current project
          
The structure of application is looking like this:
    +-project  <- Main entrypoint of the project
      +-service1  <- Service - web resource which uses only one ip address
      +-service2
      +-...
      +-serviceN
        +-Main.py           <- File which contains the code to run the service
        +-.env              <- Environment file contains data, which hasn't to be stored in the code
        +-requirements.txt  <- File which contains the requirements and dependencies
        +-Dockerfile        <- Code to containerize service using Docker. Create only with -d flag
        +-log.ini           <- File which contains the logging configuration
        +-application1        <- Application - part of the service which is usually uses to collect all code with one theme 
        |                        (For example, a users application, cart application, etc.) 
        +-application2        
        +-...
        +-applicationN
          +-__init__.py          <- __init__.py will run only once. So, you can put there code like creating consts, connecting
          |                         to database, configuring logging, etc.
          +-crud.py              <- CRUD operations
          +-models.py            <- Models of database (It won't be created if you will use -no-sql flag)
          +-shemas.py            <- Schemas of requests (It will be create only if you will use FastAPI)
          +-views.py             <- Endpoints of the application
          +-tests.py             <- Tests
          +-conftests.py         <- Test configurations (It will create automatically if your application is asyncronous and you 
                                    are using PyTest)''')

if __name__ == '__main__':
    print_help()