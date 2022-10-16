# _*_ coding:utf-8 _*_
"""
@Time: 2022/8/23 16:38
@Author: lijian
@Des： 基本路由
"""

from fastapi import APIRouter, Path, Query, Body, Form, Header, Cookie ,Request

router = APIRouter()
from api.login import index, login
from typing import List
from pydantic import BaseModel,Field
from api.test_redis import test_myredis, test_my_redis_depends

ApiRouter = APIRouter(prefix="/v1", tags=["api路由"])




ApiRouter.get('/index', tags=["api路由"], summary="注册接口")(index)

ApiRouter.post("/login", tags=["api路由"], summary='登录接口')(login)

ApiRouter.get("/test/my/redis", tags=["qpi路由"], summary="fastapi的state方式")(test_myredis)

ApiRouter.get("/test/my/redis/depends", tags=["qpi路由"], summary="依赖注入方式")(test_my_redis_depends)

