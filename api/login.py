# _*_ coding:utf-8 _*_
"""
@Time: 2022/8/30 20:30
@Author: lijian
@Des：登录测试
"""

from typing import List
from pydantic import BaseModel


class Login(BaseModel):
    username: str
    paasword: str
    user: List[int]


def index(age: int=80):
    return {"fun": "/index", "age": age}

def login(data: Login):
    return data