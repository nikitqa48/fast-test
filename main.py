from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile
from middleware import api_key_auth
from models import Docker

app = FastAPI()


@app.post('/api/python/test/', dependencies=[Depends(api_key_auth)])
def check_code(file: UploadFile = File()):
    docker = Docker()
    docker.create_testfile(file)
    docker.run_container('django')
    return {'result': docker.result}
