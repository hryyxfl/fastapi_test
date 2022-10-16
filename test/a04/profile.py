# _*_ coding:utf-8 _*_
"""
@Time: 2022/9/6 12:51
@Author: lijian
@Des：
"""


from fastapi import APIRouter, Path


router = APIRouter(prefix='/profile', tags=["资料管理"])




@router.get("",summary="查看所有资料")
def get_profile_list():
    return "get_profile_list"


@router.get("/{pid}",summary="查看指定profile")
def get_one_profile(pid: int = Path(...)):
    return f"get_one_profile{pid}"