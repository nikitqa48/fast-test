import subprocess
import os
import shutil


class Docker:
    def __init__(self):
        self.containers = os.listdir('src/tests')

    def create_testfile(self, file):
        with open(f'src/tests/django/tests/test.py', 'wb') as buffer:
            return shutil.copyfileobj(file.file, buffer)

    def __run_container(self, container: str):
        process = subprocess.run(
            f'docker-compose -f src/tests/{container}/docker-compose.yml up -t 190',
            shell=True,
            stdout=subprocess.PIPE
        )
        self.result = process
        return process

    def run_container(self, name: str):
        if name in self.containers and os.path.exists(f'src/tests/{name}/tests/test.py'):
            return self.__run_container(name)


