import subprocess
import os
import shutil


class Docker:
    def __init__(self):
        self.containers = os.listdir('src/courses')

    def create_testfile(self, file):
        with open(f'src/courses/django/files/test.py', 'wb') as buffer:
            return shutil.copyfileobj(file.file, buffer)

    def __run_container(self, container: str):
        process = subprocess.run(
            f'docker-compose -f src/courses/{container}/docker-compose.yml run web django-admin startproject example',
            shell=True,
            stdout=subprocess.PIPE
        )
        self.result = process
        return process

    def run_container(self, name: str):
        return self.__run_container(name)
        # if name in self.containers and os.path.exists(f'src/courses/{name}/files/test.py'):
        #     return self.__run_container(name)


