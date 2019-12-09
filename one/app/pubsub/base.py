import redis


class RedisSubPub:
    def __init__(self, host='localhost', port=6379, password='1234', pub='redsnow', sub='redsnow', db=0):
        pool = redis.Connection(host=host, port=port, password=password, db=db)
        self._con = redis.StrictRedis(connection_pool=pool)
        self.pub = pub
        self.sub = sub
        self._sub = None

    def public(self, msg):
        if self.pub:
            self._con.publish(self.pub, msg)  # 开始发布消息
            return True
        return False

    def subscribe(self):
        if self.sub:
            self._sub = self._con.pubsub()  # 开始订阅
            self._sub.subscribe(self.sub)  # 订阅频道
            self._sub.parse_response()  # 准备接收
            return self._sub


if __name__ == "__main__":
    a = RedisSubPub()
    a.subscribe()

