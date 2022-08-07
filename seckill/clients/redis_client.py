import redis
from mysite import settings


class RedisClient(object):
    _instance = None

    def __init__(self):
        raise RuntimeError("Call  instance() instead. This is a singleton class")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print("Creating a new RedisClient singleton")
            cls._instance = redis.StrictRedis(
                host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0
            )
        return cls._instance

    def get(self, key):
        return self._instance.get(key)

    def set(self, key, value):
        return self._instance.set(key, value)
