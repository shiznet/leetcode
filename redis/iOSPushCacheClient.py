import argparse
from TokenBeans import TokenBeans
from redisProxy import redisproxy
import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
#redisHosts={"host":"127.0.0.1","port":6379}
#r = redis.StrictRedis(host='192.168.200.49',port=6379,db=0)
#r = redisproxy(**redisHosts)
ENV = ("test", "dev", "online")


def init(args):
    redisHost = args.host
    redisPort = args.port
    if NotBlank(redisHost):
        pass
    else:
        redisHost = "127.0.0.1"
    if redisPort is None or redisPort <= 0:
        redisPort = 6379
    global r
    hosts = {"host": redisHost, "port": redisPort}
    r = redisproxy(**hosts)
    env = args.env
    if env in ENV:
        global prefix, uidprefix, tokenprefix, dndprefix
        if env == "online":
            prefix = ""
            uidprefix = "iOSPMUid:"
            tokenprefix = "iOSPMToken:"
            dndprefix = "iOSPMDND:"
        else:
            prefix = env
            uidprefix = env + "_iOSPMUid:"
            tokenprefix = env + "_iOSPMToken:"
            dndprefix = env + "_iOSPMDND:"
    else:
        if env is not None:
            logging.info('Invalid env type.env={}'.format("" + env))
        else:
            logging.info('Invalid env type.env=None')


def recurseUid(uid):
    logging.debug("\nrecurseuid=" + uid)
    if NotBlank(uid):
        tokens = traceUid(uid)
        if tokens is not None:
            printAll(*tokens)
        else:
            logging.info("uid={} has no binded token.".format(uid))
    else:
        logging.info("uid's blank")


def recurseToken(token):
    logging.debug("\nRecurseToken=" + token)
    if NotBlank(token):
        uids = traceToken(token)
        if uids is not None:
            printAll(*uids)
        else:
            logging.info("token={} has no binded uid".format(token))
    else:
        logging.info("token's blank")


def traceUid(uid):
    if uid is not None and uid != '':
        global uidprefix, r
        uidKey = uidprefix + uid
        logging.debug("uidkey=" + uidKey)
        tokens = r.smembers(uidKey)
        if tokens is not None:
            printAll(*tokens)
            for token in tokens:
                tuMap = r.hgetall(tokenprefix + token).toMap()
                printAll(**tuMap)
                return tokens
        else:
            logging.info("uid={} has no token".format(uid))
    else:
        logging.info("Blank uid")
    return None


def traceToken(token):
    '''
    print all information relative to the token.
    '''
    if token is not None and token != '':
        token = token.upper()
        global r
        tokenKey = tokenprefix + token
        logging.debug("tokenKey=" + tokenKey)
        tuMap = r.hgetall(tokenKey)
        if tuMap is not None:
            uidlist = tuMap.keys()
        if tuMap is None or any(tuMap) == False:
            logging.debug("token={}'s no info".format(token))
        else:
            logging.debug("\ntoken={}".format(token))
            printAll(**tuMap)
    else:
        logging.info("token blank.")
    return uidlist


#def cleanUPToken(token)

def genTokenKey(token):
    return tokenprefix + token


def genUidKey(uid):
    return uidprefix + uid


def process(opt, uid=None, token=None):
    pass


def NotBlank(str):
    if str is not None and str != "":
        return True
    else:
        return False


def printAll(*list, **dict):
    '''
    Print details of list or dict.
    '''
    if list is not None:
        for a in list:
            logging.info("\tlist:{}".format(a))
    if dict is not None:
        for key in dict:
            logging.info("\t{}={}".format(key, dict[key]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--operation",
                        help="Specific operation.Such as del modify.Default's lookup")
    parser.add_argument("-u", "--uid", help="")
    parser.add_argument("-t", "--token", help="")
    parser.add_argument("-e", "--env", help="")
    parser.add_argument("-s", "--host", help="redis host")
    parser.add_argument("-p", "--port", help="redis port")
    args = parser.parse_args()
    token = args.token
    uid = args.uid
    opt = args.operation
    env = args.env
    global prefix
    if token is None and uid is None:
        print "token or uid should not be None at the same time."
    if env is None:
        print "Please set env."
    init(args)
    recurseUid(uid)
    recurseToken(token)
