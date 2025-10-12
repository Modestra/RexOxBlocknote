import ast
import re
def main():
    result = {}
    file = "params.py"
    with open(file, 'r') as f:
        file_content = f.read()
        matches = re.findall(r'(\w+)\s*=\s*(.+)', file_content)
        for keys, variables in matches:
            result.setdefault(keys, variables)
        f.close()

if __name__ == "__main__":
    main()