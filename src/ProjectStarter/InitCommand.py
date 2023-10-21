from . import Command

class InitCommand(Command):
    def init(self):
        return '''Usage: ProjectStarter init [PARAMS] 

This is a script to make porject creation and development faster. Uses PyProject.toml

Available subcommands:
    init                Create a new PyProject.toml and initialize the project in the current directory
    create <object>     Creates a serive or application in the current project
          
Available Options:
    -h, --help          Show this help message
    -v, --version       Show version

The structure of application will look like this:
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
                                    are using PyTest)'''