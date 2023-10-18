from ProjectStarter import PyProject

class Project:
    '''
    This class represents a project
    '''

    def __init__(self, py_project_path: str):
        try:
            self.py_project = PyProject(py_project_path)
        except FileNotFoundError:
            raise FileNotFoundError(f'could not load project {py_project_path}')
        