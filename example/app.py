import os
import sys
from modchem import commands 
def main():
    os.environ.setdefault('MODCHEM_APP_PARAMS', "example.params")
    commands.execute_command_line(sys.argv)

if __name__ == '__main__':
    main()