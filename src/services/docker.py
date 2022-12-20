import subprocess
import os


class Docker:
    def __init__(self):
        self.containers = os.listdir('src/courses')

    def __run_container(self, framework: str, app: str):
        process = subprocess.run(
            f'docker-compose -f src/courses/{framework}/{app}/docker-compose.yml run web python manage.py test',
            shell=True,
            stdout=subprocess.PIPE
        )
        self.result = process
        return process

    def run_container(self, name: str, app: str):
        return self.__run_container(name, app)
        # if name in self.containers and os.path.exists(f'src/courses/{name}/files/test.py'):
        #     return self.__run_container(name)


docker = Docker()
