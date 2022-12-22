import redis as red


class Redis:
    def __init__(self, host, port, db):
        self._connection = red.StrictRedis(host=host, port=port, db=db, charset="utf-8", decode_responses=True)

    def publish(self, channel, message):
        return self._connection.publish(channel, message)

    def pubsub(self):
        return self._connection.pubsub()

    def subscribe(self, channel):
        sub = self.pubsub()
        sub.subscribe(channel)
        for message in sub.listen():
            if type(message['data']) is not int:
                return message['data']


redis = Redis(host='redis', port=6379, db=0)
