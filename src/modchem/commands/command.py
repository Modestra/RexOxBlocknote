from modchem.core.project import Project
class BaseCommand:
    name=""
    description=""

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def execute():
        print("Инициализация команды")

class CreateProjectCommand(BaseCommand):

    def __init__(self, name, description):
        super().__init__(name, description)
    
    def execute(self, title: str):
        project = Project(name=title)
        project.create()
        print(f"Initialisation {self.name} - {self.description}")

