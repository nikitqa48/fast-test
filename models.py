import subprocess
import os
import shutil


class Docker:
    def __init__(self):
        self.containers = os.listdir('test_dir')

    def create_testfile(self, file):
        with open(f'test_dir/django/test.py', 'wb') as buffer:
            return shutil.copyfileobj(file.file, buffer)

    def __run_container(self, container: str):
        process = subprocess.run(
            f'docker-compose -f test_dir/{container}/docker-compose.yml up',
            shell=True,
            stdout=subprocess.PIPE
        )
        self.result = process
        return process

    def run_container(self, name: str):
        if name in self.containers and os.path.exists(f'test_dir/{name}/test.py'):
            return self.__run_container(name)


