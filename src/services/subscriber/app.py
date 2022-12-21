import json
import redis
from src.services.folders import FolderService
from src.services.docker import docker

r = redis.StrictRedis(host='redis', port=6379, db=0, charset="utf-8", decode_responses=True)


def subscribe():
    sub = r.pubsub()
    sub.subscribe('user')
    for message in sub.listen():
        data = message.get('data')
        if type(message['data']) is not int:
            data = json.loads(data)
            folder = FolderService(data['framework'], data['app'])
            folder.write_user_code(data['path'], data['code'])
            docker.run_container(data['framework'], data['app'])
            folder.return_filedata()


while True:
    subscribe()
