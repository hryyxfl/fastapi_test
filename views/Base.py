# _*_ coding:utf-8 _*_
"""
@Time: 2022/8/30 21:33
@Author: lijian
@Des： 视图路由
"""

from fastapi import APIRouter
from starlette.responses import HTMLResponse

from views.home import home , reg_page, result_page



ViewsRouter = APIRouter()


ViewsRouter.get('/item/{id}', response_class=HTMLResponse)(home)

ViewsRouter.get("/reg", response_class=HTMLResponse)(reg_page)
ViewsRouter.post("/reg/form",response_class=HTMLResponse)(result_page)