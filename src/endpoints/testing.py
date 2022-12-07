from fastapi import APIRouter
from fastapi import Depends
from src.middleware import api_key_auth
from src.services.docker import docker
from src.services.folders import FolderService
from database import models

test = APIRouter()

@test.post('/api/python/test/{name}/', dependencies=[Depends(api_key_auth)])
def test_code(name: str, item: models.Item):
    # redis.set('user', item.json())
    service = FolderService(name, item.app)
    service.write_user_code(item.path, item.code)
    docker.run_container(name, item.app)
    service.return_filedata()
    return {'result': docker.result}