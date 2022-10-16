# _*_ coding:utf-8 _*_
"""
@Time: 2022/9/22 17:05
@Author: lijian
@Des：配置文件
"""


from pydantic import BaseSettings
# 文档： https://pydantic-docs.helpmanual.io/usage/settings/


class Settings(BaseSettings):
    # debug模式
    debug: bool = True

    # jwt 加密的key  密钥还有可以根据环境生成
    jwt_secret_key: str = "abcdefghijklmn"
    # jwt 加密算法
    jwt_algorithm: str = 'HS256'
    #  token过期时间 单位：秒
    jwt_exp_seconds: int = 60 * 60



settings = Settings()

