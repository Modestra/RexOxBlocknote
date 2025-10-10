import os

class BaseProgram:
    """Base template of Appication Elements"""
    config = {}

    def __init__(self, *args, **kwargs):
        self.config.update(kwargs)

    def get_config(self):
        return self.config
    
    def create(self, *args, **kwargs):
        self.config.update(**kwargs)
        return self.config

class Application(BaseProgram):

    def create(self, name: str, params: str, dir: str):
        os.mkdir(dir)
        return super().create(name, params, dir)