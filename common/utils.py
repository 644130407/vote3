import hashlib


def getMd5(data):
    return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()