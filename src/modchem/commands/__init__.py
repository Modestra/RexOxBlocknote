import sys
import os
from modchem.templates import load_app_template, load_params_template
from modchem.core import app
from modchem.commands.command import CreateProjectCommand
from argparse import ArgumentParser
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
        os.environ.setdefault("MODCHEM_APP_NAME", dir)
        _app = app.Application()
        try:
            _app.create(name=dir, params='params.py', dir=base_dir)
            load_app_template()
            load_params_template()
        except FileExistsError:
            sys.stderr.write(f"Путь {base_dir} уже занят")

def execute_command_line(argv):
    parser = ArgumentParser(description="Initial Experiment Environment")
    parser.add_argument("command", help="Select command")
    parser.add_argument("name", help="Set Name")
    _argv = parser.parse_args()
    if 'create_project' == _argv.command:
        CreateProjectCommand("create_project", "Creating Project").execute(title=_argv.name)

def execute_experiment_environment():
    parser = ArgumentParser(description="Initial Experiment Environment")
    parser.add_argument("project_name", help="Environment name")
    argv = parser.parse_args()
    execute = ExecuteEnvironment(args=argv._get_kwargs()[0][1])
    execute.initialize()