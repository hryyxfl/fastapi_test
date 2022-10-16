# _*_ coding:utf-8 _*_
"""
@Time: 2022/9/20 21:22
@Author: lijian
@Des：
"""

from fastapi import Body, Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from models8 import UserInfo, UserInDB, UserLogin, UserSignUp
from libs.db_lib import db
from libs.hash_lib import hash_tool
from config8 import settings
from auth8 import auth_depend, create_access_token

from uvicorn import run

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'))


@app.get("/")
def home():
    return {"hellod": "world - a08"}


@app.post("/signup", summary="注册接口")
def signup(form_data: UserSignUp = Body(...)):
    # 拿到前端传过来的数据
    username = form_data.username
    password = form_data.password

    # 校验这个数据

    # 根据用户名去数据库里面查对应的user
    user = db.get_or_none(username)

    # 如果已经有了，就返回错误信息
    if user is not None:
        return {"msg": "当前用户名已经被占用了"}
    # 保存到数据库
    encode_pwd = hash_tool.encrypt_password(password)
    user = UserInDB(username=username, password=encode_pwd)
    db.save(user)
    #  给前端响应信息
    return {"msg": "ok"}


@app.post("/login", summary="登录接口")
def login():
    return {"msg": "login"}


def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    #  第一步 拿到 用户名和密码 ，校验
    username= form_data.username
    password=form_data.password

    #  第二步 通过用户名去数据库中查找到对应的user
    user = db.get_or_none(username)
    if user is None:
        return {"msg": "登陆失败,用户名与密码不匹配"}

    # 第三步检查密码
    if not hash_tool.check_password(user.password,password):
        return {"msg": "登陆失败,用户名与密码不匹配"}

    # 第四步 生成token
    #   Authorization: bearer header.payload.sign
    token = create_access_token({"username": username})

    #  给前端响应信息
    return {"access_token": token, "token_type": "bearer"}


if settings.debug:
    app.post("/token", summary="获取token接口")(get_token)


@app.get("/me",summary="个人信息")
def get_my_info(me: UserInDB = Depends(auth_depend)):
    user_info = UserInfo(**me.dict())
    return {"msg": user_info}

@app.get("/vip",summary="查看vip信息",dependencies=[Depends(auth_depend)])
def get_vip_info():
    return {"msg": "vip info"}


if __name__ == '__main__':
    # run("app:app", port=8888, reload=True)
    run("main:app", port=8888, reload=True)
