# _*_ coding:utf-8 _*_
"""
@Time: 2022/9/6 13:20
@Author: lijian
@Des：
"""
from typing import Dict, List
from fastapi import Depends,FastAPI,Query
from uvicorn import run

app = FastAPI()


@app.get("/")
async def read_root():
    return {"hellod":"world"}

def paginator(page: int = Query(1,gt=0, description='当前页码'),
    page_szie: int = Query(10, gt=0, le=100, description="每页数量", alias="pageSize")) -> Dict[str, int]:
    return {"page":page, "page_szie":page_szie}

def order_by_filed(order_by: List[str] = Query(...,description="按给定的字段排序，可以输入多个字段")):
    return {"orde":order_by}

def paginator_with_order(pg: Dict[str,int] = Depends(paginator), order: List[str] = Depends(order_by_filed)):
    return {"pg": pg, "order": order}


@app.get("/depends/page",summary="依赖的简单使用 - 分页")
def get_paginator(pg:Dict[str,int] = Depends(paginator)):
    return {"mag": pg}
    
@app.get("/depends/order", summary="依赖的简单使用 - 排序")
def get_order(order: List[str] = Depends(order_by_filed)):
    return {"msg": order}


@app.get("/depends/pg_plus", summary="依赖的嵌套 - 分页+排序")
def get_paginator_plus(pg_plus: dict = Depends(paginator_with_order)):
    return {"msg": pg_plus}

if __name__ == '__main__':
    # run("app:app", port=8888, reload=True)
    run("main:app", port=8888, reload=True)
