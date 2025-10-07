import sys
import os
from modchem.templates import load_app_template, load_params_template
from modchem.core import app
from modchem.core import params
from argparse import ArgumentParser
from modchem.core.logger import logger
class ExecuteEnvironment:
    """Класс инициализации виртуальной среды"""
    args = ""
    commands = []
    def __init__(self, args):
        self.args = args
        
    def initialize(self):
        self._execute(self.args)

    def _execute(self, dir: str):
        base_dir = os.path.join(os.getcwd(), dir)
        os.environ["MODCHEM_APP_NAME"] = dir
        try:
            _app = app.register_app(name=dir, params='params.py', dir=base_dir)
            _app.create()
            load_app_template()
            load_params_template()
        except FileExistsError:
            sys.stderr.write(f"Путь {base_dir} уже занят")

@logger(logfile="command.log")
def execute_command_line(argv):
    pass

def execute_experiment_environment():
    parser = ArgumentParser(description="Initial Experiment Environment")
    parser.add_argument("project_name", help="Environment name")
    argv = parser.parse_args()
    execute = ExecuteEnvironment(args=argv._get_kwargs()[0][1])
    execute.initialize()