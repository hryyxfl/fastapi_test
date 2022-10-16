# _*_ coding:utf-8 _*_
"""
@Time: 2022/9/6 12:50
@Author: lijian
@Des：
"""


from fastapi import FastAPI
from user import router as user_router
from profile import router as profile_router
from uvicorn import run

app = FastAPI()



app.include_router(user_router)
app.include_router(profile_router)




if __name__ == '__main__':
    # run("app:app", port=8888, reload=True)
    run("main:app", port=8888, reload=True)