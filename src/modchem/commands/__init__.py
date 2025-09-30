import sys
from .command import BaseCommand
class ExecuteEnvironment:
    """Класс инициализации виртуальной среды"""
    args = list
    commands = []
    def __init__(self, args):
        self.args = args
        self.commands.append(BaseCommand(
            name= "ExecuteExpetiment",
            description= "Запуск виртуальной среды эксперимента"
        ).dict_parser())
        
    def initialize(self):
        if "-h" in self.args:
            self.help_info()

    def help_info(self):
        """Вывести информацию о текущих командах"""
        sys.stdout.write("Команды\n")
        for command in self.commands:
            self.info(command)
        
    def info(self, command):
        sys.stdout.write(f"\t{command["name"]} - {command["description"]}")