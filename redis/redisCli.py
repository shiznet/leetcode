from redisProxy import redisproxy

hosts = {"host": "127.0.0.1", "port": 6379}
r = redisproxy(**hosts)
print r.hgetall("iOSPMToken:token")
r.scan(0,"abc",10)
