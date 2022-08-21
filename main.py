import subprocess
from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile
import os
import shutil
from middleware import api_key_auth

app = FastAPI()


@app.post('/api/python/test/', dependencies=[Depends(api_key_auth)])
def check_code(file: UploadFile = File()):
    with open(f'test_dir/django/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    process = subprocess.run(
        'docker-compose -f test_dir/django/docker-compose.yml up',
        shell=True,
        stdout=subprocess.PIPE
    )
    return {'result': process}
