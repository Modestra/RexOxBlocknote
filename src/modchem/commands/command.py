from modchem.core.project import Project
from modchem.core.params import params
class BaseCommand:
    name=""
    description=""

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def execute():
        pass

class CreateProjectCommand(BaseCommand):

    def __init__(self, name, description):
        super().__init__(name, description)
    
    def execute(self, title: str):
        project = Project(name=title)
        project.create()

class DeleteProjectCommand(BaseCommand):

    def __init__(self, name, description):
        super().__init__(name, description)
    
    def execute(self, title: str):
        project = Project(name=title)
        project.delete()

class ReadParamsCommand(BaseCommand):

    def __init__(self, name, description):
        super().__init__(name, description)
    
    def execute(self):
        params.update_params()
        params.get_config()

