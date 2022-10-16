# _*_ coding:utf-8 _*_
"""
@Time: 2022/9/17 14:31
@Author: lijian
@Des：
"""

from pathlib import Path

from fastapi import Depends, FastAPI
from starlette.requests import Request
from uvicorn import run

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

media_dir = Path(__file__).absolute().parent

class FolderMaker:
    def __init__(self,upload_to:str):
        self.upload_to = upload_to
        self.dir_path = None

    def __call__(self, req:Request):
        dir_path = media_dir / self.upload_to
        # 检查目录存不存在
        self.dir_path = str(dir_path)

        return self

    def upload_to_qiniu(self):
        print("我是要上传到七牛的")

@app.get("/upload/image",summary="类作为依赖 - 上传图片")
def auth_admin(folder_maker: FolderMaker = Depends(FolderMaker("image"))):
    print(folder_maker.dir_path)
    folder_maker.upload_to_qiniu()
    return {"mag": "ok"}

@app.get("/upload/pdf",summary="类作为依赖 - 上传pdf")
def auth_admin(dir_name: FolderMaker = Depends(FolderMaker("pdf"))):
    return {"mag":dir_name}


if __name__ == '__main__':
    # run("app:app", port=8888, reload=True)
    run("main:app", port=8888, reload=True)