import os
from modchem.core.app import BaseProgram

class Project(BaseProgram):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_config(self):
        return super().get_config()

    def create(self):
        if self.config.get('name') is None:
            return ValueError("Project hasn't name")
        os.mkdir(os.path.join(os.getcwd(), self.config.get('name')))
        
