import json

from fastapi import APIRouter
from fastapi import Depends
from src.middleware import api_key_auth
from src.services.docker import docker
from src.services.folders import FolderService
from database import models
from src.services.publish import publish
test = APIRouter()


@test.post('/api/python/test/{name}/', dependencies=[Depends(api_key_auth)])
def test_code(name: str, item: models.Item):
    data = json.dumps({'path': item.path, 'code': item.code, 'app': item.app, 'framework': name})
    publish('user', data)

    # r.set('user', item.json())
    # service = FolderService(name, item.app)
    # service.write_user_code(item.path, item.code)
    # docker.run_container(name, item.app)
    # service.return_filedata()
    # return {'result': docker.result}