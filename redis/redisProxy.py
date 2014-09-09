import redis
from TokenBeans import TokenBeans


class redisproxy(object):
    def __init__(self,
                 **redishosts):
        #self.r = redis.StrictRedis(host=redishosts["host"],port=redishosts["port"],db=0)
        self.r = redis.Redis(host=redishosts["host"], port=redishosts["port"], db=0)

    def hgetall(self, tokenKey):
        uidsMap = self.r.hgetall(tokenKey)
        if uidsMap is None:
            print "[{}]No rec found.key={}".format(
                "hgetall", tokenKey)
        tb = TokenBeans(**uidsMap)
        return tb.toMap()

    def smembers(self, uidKey):
        tokens = self.r.smembers(uidKey)
        #if tokens is None or tokens

    def get(self, key):
        return self.r.get(key)

    def delete(self, key):
        self.r.delete(key)  #del is reserved word for python

    def set(self, key, value):
        self.r.set(key, value)

    def scan(self, cursor=0, pattern=None, count=None):
        result = self.r.scan(cursor, pattern, count)
