# _*_ coding:utf-8 _*_
"""
@Time: 2022/8/25 17:17
@Author: lijian
@Des： 工具函数
"""

import hashlib
import uuid


def random_str():


    only = hashlib.md5(str(uuid.uuid1()).encode(encoding='UTF-8')).hexdigest()
    return str(only)