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
        f'pytest -rx test_dir/django/{file.filename}',
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    os.remove(f'test_dir/django/{file.filename}')
    return {'result': process}

