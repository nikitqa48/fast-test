import json
import redis
from src.services.folders import FolderService

r = redis.StrictRedis(host='redis', port=6379, db=0, charset="utf-8", decode_responses=True)


def subscribe():
    sub = r.pubsub()
    sub.subscribe('user')
    for message in sub.listen():
        data = message.get('data')
        if type(message['data']) is not int:
            data = json.loads(data)
            service = FolderService(data['framework'], data['app'])
            service.write_user_code(data['path'], data['code'])


while True:
    subscribe()
