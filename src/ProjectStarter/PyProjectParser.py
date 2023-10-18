import toml

class PyProject:
    '''
    Class to parse a pyproject.toml file and gather information about the project in it
    '''

    def __init__(self, path: str):
        self.path = path

        try:
            self.data = toml.loads(self.path)
        except FileNotFoundError:
            raise FileNotFoundError(f'could not load project {self.path}')
        
    @property
    def name(self):
        try:
            return self.data['project']['name']
        except KeyError:
            self.data['project']['name'] = 'New project'
            return 'New project'
        
    @property
    def framework(self):
        try:
            return self.data['project']['framework']
        except KeyError:
            raise Exception('Framework not specified in pyproject.toml. Please specify it (see --help)')

    def get_section(self, section_name: str = ...):
        try:
            return self.data[section_name]
        except KeyError:
            raise KeyError(f'could not find section {section_name} in {self.path}')

    def set_section(self, section_name: str = ..., data: dict = ...):
        self.data[section_name] = data