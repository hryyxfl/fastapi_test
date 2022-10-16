# _*_ coding:utf-8 _*_
"""
@Time: 2022/8/27 16:11
@Author: lijian
@Des：  路由聚合
"""


from api.Base import ApiRouter
from views.Base import ViewsRouter
from fastapi import APIRouter



AllRouter = APIRouter()

#  视图路由
AllRouter.include_router(ViewsRouter)

# API路由
AllRouter.include_router(ApiRouter)

