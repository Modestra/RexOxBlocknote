from modchem.core.app import BaseProgram

class AppParams(BaseProgram):
    params = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.params = self.config.copy()
    
    def get_config(self):
        return self.params
    
    def update_params(self, *args, **kwargs):
        super().create(*args, **kwargs)
        self.params.update(self.config)

params = AppParams()