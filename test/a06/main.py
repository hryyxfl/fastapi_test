# _*_ coding:utf-8 _*_
"""
@Time: 2022/9/16 22:28
@Author: lijian
@Des：
"""


from fastapi import FastAPI, Depends,Header,HTTPException
from uvicorn import run


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World a06"}


def auth_depend(auth: str = Header(...,description="请求头认证",alias="X-Auth")):
    if auth != "admin":
        raise HTTPException(status_code=401, detail="认证不通过")


@app.get("/depens/auth",summary="路径操作装饰器依赖项", dependencies=[Depends(auth_depend)])
def auth_admin():
    return {"msg":"ok"}


if __name__ == '__main__':
    # run("app:app", port=8888, reload=True)
    run("main:app", port=8888, reload=True)