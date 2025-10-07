import os

class Application:
    app_name = ""
    app_params = ""
    path_dir = ""
    log_dir = ""
    project_list = []

    def __init__(self):
        pass

    def set_app(self, name: str, params: str, path_dir: str):
        self.app_name = name
        self.app_params = params
        self.path_dir = path_dir
        self.log_dir = os.path.join(self.path_dir, "logs")

    def create(self):
        os.mkdir(self.path_dir)

def register_app(name: str, params: str, dir: str):
    app = Application()
    app.set_app(name=name, params=params, path_dir=dir)
    return app