import json
from src.services.redis import redis
from src.services.folders import FolderService
from src.services.docker import docker


def subscribe():
    sub = redis.pubsub()
    sub.subscribe('user')
    for message in sub.listen():
        data = message.get('data')
        if type(message['data']) is not int:
            data = json.loads(data)
            folder = FolderService(data['framework'], data['app'])
            folder.write_user_code(data['path'], data['code'])
            docker.run_container(data['framework'], data['app'])
            folder.return_filedata()
            user_data = {
                'code': docker.result.returncode,
                'error': docker.result.stderr.decode(),
                'output': docker.result.stdout.decode()
            }
            redis.publish(data['user_key'], json.dumps(user_data))


while True:
    subscribe()
