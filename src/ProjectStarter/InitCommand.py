import Command
from TemplateConfig import env
import ArgsParser
import sys
import pathlib

class InitCommand(Command.Command):
    def help(self):
        return '''Usage: ProjectStarter init [PARAMS] [DIRECTORY]

Creates a new PyProject.toml.
          
Available Options:
    -h, --help              Show this help message
    -n, --name              Name of the project
        --project-version   Version of the project
'''

    def init_project(
                self, 
                path: pathlib.Path,
                project_name: str = ...,
                project_version: str = ...,
            ):
        pyproject = env.get_template('./pyproject_template.toml').render(
            project_name=project_name,
            project_version=project_version,
            services=[],
        )

        pyproject_path = path / 'pyproject.toml'
        if pyproject_path.exists():
            ans = input('PyProject.toml already exists. Continue? (y/n): ')
            if not (ans.lower() == 'y' or ans.lower() == 'yes'):
                sys.exit(0)

        with open(pyproject_path, 'w') as f:
            f.write(pyproject)

    def run(self, args: list[str]):
        try:
            parser = ArgsParser.ArgParser()
            parser.search_arg('-h', is_flag=True)
            parser.search_arg('--help', is_flag=True)
            parser.search_arg('-n')
            parser.search_arg('--name')
            parser.search_arg('--project-version')

            data, unparsed = parser.parse(args)
            print(data)

            if data['-h'] or data['--help']:
                print(self.help())
                sys.exit(0)

            creation_path = pathlib.Path('.')
            if len(unparsed) > 0:
                creation_path = pathlib.Path(unparsed[0])

            # If you will use or with None and not none value, python will return value
            # 'fdkjl' or None => 'fdkjl'
            # None or 'fdkjl' => 'fdkjl'
            # None or None => None

            project_name = data.get('-n') or data.get('--name')
            project_version = data.get('--project-version')

            self.init_project(
                creation_path,
                project_name=(project_name or 'New project'),
                project_version=(project_version or '0.0.1'),
            )
            sys.exit(0)
        except ValueError:
            print(self.help())
            sys.exit(2)