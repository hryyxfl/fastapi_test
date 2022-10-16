# _*_ coding:utf-8 _*_
"""
@Time: 2022/8/25 13:33
@Author: lijian
@Des：  事件监听
"""

from typing import Callable
from fastapi import FastAPI
from database.mysql import register_mysql
from database.redis import sys_cache
from aioredis import Redis


def startup(app: FastAPI) -> Callable:
    """
    FastApi启动完成事件
    :param app: FastApi
    :return: app_start
    """

    async def app_start() -> None:
        # app启动完成后触发
        print("启动完毕")
        await register_mysql(app)
        # 注入缓存到 app state
        # app.state.cache = await sys_cache()
    return app_start


def stopping(app: FastAPI) -> Callable:
    """
    FastApi停止事件
    :param app:  Fastapi
    :return:  stop_app
    """

    async def stop_app() ->None:
        # app停止时触发
        print("停止")
        pass
    return stop_app
