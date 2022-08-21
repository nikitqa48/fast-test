from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import subprocess


class Docker:

    def __init__(self):
        self.status = 'active'
        self.file = ''
