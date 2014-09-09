#! /usr/bin/python2.5
# -*- coding: cp936 -*-
__author__ = 'hzliwenjia@corp.netease'
import argparse
from redisProxy import redisproxy


def countKey(r, pattern):
    cursor = 0
    count = 100
    counter = 0
    while True:
        result = r.scan(cursor, parser, count)
        cursor = result["cursor"]
        counter += result["cnt"]
        if cursor <= 0:
            break
    return counter


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--host", help="redis host")
    parser.add_argument("-p", "--port", help="redis port")
    parser.add_argument("--pattern")
    args = parser.parse_args()
    host = args.host
    port = args.port
    pattern = args.pattern
    if port is None:
        port = 6379
    r = redisproxy({"host": host, "port": port})
    print countKey(r, pattern)
