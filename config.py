# _*_ coding:utf-8 _*_
"""
@Time: 2022/8/25 14:30
@Author: lijian
@Des：基本配置文件
"""

import os.path
from dotenv import load_dotenv,find_dotenv
from pydantic import BaseSettings
from typing import List


class Config(BaseSettings):
    #  加载环境变量
    load_dotenv(find_dotenv(), override=True)
    #  调试模式
    APP_DEBUG: bool = True

    # 项目信息
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "fastapi-demo"
    DESCRIPTION: str ="fastapi项目demo"

    # 静态资源目录
    STATIC_DIR: str = os.path.join(os.getcwd(), "static")
    TEMPLATE_DIR: str = os.path.join(STATIC_DIR, "templates")

    #跨越请求
    CORS_ORIGINS: List[str] = ['*']
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ['*']
    CORS_ALLOW_HEADERS: List[str] = ['*']


settings = Config()

