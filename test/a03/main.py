# _*_ coding:utf-8 _*_
"""
@Time: 2022/9/11 13:01
@Author: lijian
@Des：
"""
from fastapi import FastAPI
from fastapi import APIRouter, Path, Query, Body, Form, Header, Cookie ,Request
from typing import List
from pydantic import BaseModel ,Field
from user import router as user_router
from profile import router as profile_router
from uvicorn import run

ApiRouter = FastAPI()




@ApiRouter.get("/path/{num}", summary="路径参数-简单使用")
async def home(num: int=Path(...,description='这是一个路径参数')):
    return {"num": num, "data": [{"num": num, "data": []}, {"num": num, "data": []}]}

@ApiRouter.get("/path/class/{num1}/student/{num2}", summary="路径参数-多个参数")
async def home1(num1: int=Path(..., gt=0), num2: int=Path(...,gt=0)):
    return {"num1":num1, "num2":num2}

@ApiRouter.get("/query", summary="查询参数")
async def get_query(q:str=Query(... , min_length=5)):
    return q

@ApiRouter.get("/query/page", summary="查询参数-分页")
async def get_page(page: str=Query(1, description="当前页码"), page_size: int=Query(10,description="每页数量",alias="pageSize")):
    return {"page": page," page_szie": page_size}

@ApiRouter.get("/query/order", summary="查询参数-多个参数")
async def get_order(order: List[str]=Query(["id"] , description="按指定的字段排序，可以输入多个字段")):
    return order

@ApiRouter.post("/body/base", summary="body-基本使用")
async def post_body(p: str = Body(...)):
    return {"msg": p}

class Car(BaseModel):
    name : str = Field(...,description="名称")
    brabd: str = Field(...,max_length=10)
    price: float = Field(...,gt=0,description="价格", example=10)


@ApiRouter.post("/body/dict", summary="body-传一个字典")
async def post_dict(p: Car = Body(...)):
    return {"msg": p}
@ApiRouter.post("/body/list", summary="body-同时传多个个字典") #  集合 和嵌套
async def post_list(p: List[Car] = Body(...)):
    return {"msg": p}

@ApiRouter.post("/from", summary="from-表单")
async def from_data(name: str=Form(...)):
    return name

#  alias="Authorization"
@ApiRouter.post("/header", summary="获取请求头参数") #  集合 和嵌套
async def get_header_param(param: str = Header(..., description='自定义 header', alias="Authorization" )):
    """
    Authorization或authorization  docs界面不会自动发请求头  使用apipost测试
    :param param:
    :return:
    """

    return {"param": param}


@ApiRouter.get("/cookie", summary="cookie参数")
async def get_cookie_param(param: str=Cookie(None,alias="CocaCola",description="自定义cookie",example="PepsiCo")):
    """
    在header中设置”cookie“注意小写的c
    apipost测试
    :param param:
    :return:
    """
    return {"param":param}

@ApiRouter.get("/req", summary="request 对象")
async def get_rqeuest(req: Request ):
    print(req)
    return {
    "base_url":req.base_url,
    "client": req.client,
    "cookies": req.cookies,
    "headers": req.headers,
    "method": req.method,
    "path_params": req.path_params,
    "query_params": req.query_params,
    "scope": {k: str(v) for k, v in req.scope.items()},
    "url": req.url,
    "state": req.state,

    }

if __name__ == '__main__':
    # run("app:app", port=8888, reload=True)
    run("main:ApiRouter", port=8888, reload=True)

