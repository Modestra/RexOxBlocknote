import os, sys
from modchem import commands 
def main():
    """Запуск командной строки приложения"""
    os.environ.setdefault('MODCHEM_APP_SETTINGS', "project.settings")
    commands.execute_command_line(sys.argv)

if __name__ == '__main__':
    main()
    

