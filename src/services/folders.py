import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
course_dir = os.path.join(BASE_DIR, 'courses')


class FolderService:

    def __init__(self, framework: str, app: str):
        dir = os.path.join(course_dir, framework)
        self.file = None
        self.dir = os.path.join(dir, app)

    def write_user_code(self, path: str, code: str):
        dir = os.path.join(self.dir, path)
        with open(dir, "r+") as f:
            data = f.read()
            self.file = {'file': dir, 'data': data}
            f.write(code)

    def return_filedata(self):
        with open(self.file['file'], "r+") as f:
            f.truncate(0)
            data = self.file['data']
            f.write(data)
