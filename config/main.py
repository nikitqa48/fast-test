from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile
from middleware.middleware import api_key_auth
from src.tests.service import Docker

app = FastAPI()


@app.post('/api/python/test/{name}/', dependencies=[Depends(api_key_auth)])
def test_code(name: str, file: UploadFile = File()):
    docker = Docker()
    docker.create_testfile(file)
    docker.run_container(name)
    return {'result': docker.result}
