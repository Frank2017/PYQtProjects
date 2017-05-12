# coding=UTF-8
import hashlib

def getMD5(str):
    """
    返回str的MD5加密结果
    :param str: 待加密字符串
    :return: 加密后字符串
    """
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()
    pass