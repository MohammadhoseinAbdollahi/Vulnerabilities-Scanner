import os
import re

def find_imports(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return re.findall(r'^import (\S+)', content, re.MULTILINE)

def scan_directory(directory):
    imports = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                imports.update(find_imports(file_path))
    return imports

def main():
    directory = '/Users/mohammadhosein/Documents/FSTT'  # replace with your directory
    imports = scan_directory(directory)
    with open('requirements.txt', 'w') as file:
        for imp in sorted(imports):
            file.write(f'{imp}\n')

if __name__ == '__main__':
    main()