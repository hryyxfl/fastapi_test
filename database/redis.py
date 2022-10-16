# _*_ coding:utf-8 _*_
"""
@Time: 2022/9/26 21:38
@Author: lijian
@Des：  redis
"""


import aioredis
import os
from aioredis import Redis


async def sys_cache() -> Redis:


    #  从URL方式创建redis连接池
    sys_cache_pool = aioredis.ConnectionPool.from_url(
        f"redis://{os.getenv('CACHE_HOST', '127.0.0.1')}:{os.getenv('CACHE_PORT', 6379)}",
        db=os.getenv('CACHE_DB', 0),
        encoding='utf-8',
        decode_responses=True
    )

    return Redis(connection_pool=sys_cache_pool)
