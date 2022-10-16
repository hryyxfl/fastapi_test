# _*_ coding:utf-8 _*_
"""
@Time: 2022/9/6 12:35
@Author: lijian
@Des：
"""


from fastapi import APIRouter ,Path



router = APIRouter(prefix='/user',tags=['用户管理'])

#  /user
router.get("", summary="查看用户列表")
def get_user_list():
    return "user_list"



# /user/2
@router.get("/{uid}",summary='查看指定用户')
def get_one_user(uid: int = Path(...)):
    return f"get_one_user：{uid}"