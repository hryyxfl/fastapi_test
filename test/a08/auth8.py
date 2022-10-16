# _*_ coding:utf-8 _*_
"""
@Time: 2022/9/22 21:20
@Author: lijian
@Des：
"""

import traceback
from datetime import datetime,timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from config8 import settings
from libs.db_lib import db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



def create_access_token(data: dict, expires_delta: Optional[timedelta]=None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(seconds=settings.jwt_exp_seconds)
    to_encode.update({"exp": expire})
    encoded_jwt =  jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm )
    return encoded_jwt


def auth_depend(token: str = Depends(oauth2_scheme)):
    #  1。解析token中的payload信息
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        print(payload)
    except JWTError:
        exc_msg = '\n' + "-" * 40 + "  catch some exceptions  " + "-" * 40 + '\n'
        exc_msg += traceback.format_exc()+'\n'
        local_vars = locals()
        del local_vars['exc_msg']
        exc_msg+=f"{local_vars}" + '\n'
        exc_msg+= "_" *100
        print(exc_msg)
        raise HTTPException(status_code=401, detail="token已经失效,请重新登录！")

    # 2.根据payload中的信息去数据库中找到对应的用户
    username = payload.get("username")
    print(username)
    user =  db.get_or_none(username)
    if user is None:
        raise HTTPException(status_code=401, detail="认证不通过")
    return user
