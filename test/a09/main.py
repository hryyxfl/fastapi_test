# _*_ coding:utf-8 _*_
"""
@Time: 2022/9/30 20:29
@Author: lijian
@Des：
"""
import time

from fastapi import Body, FastAPI, Query, Request

from uvicorn import run

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    if request.headers["host"] == "127.0.0.1:8000":
        request.state.user="admin"
        print(request.url)

    # scope receive send
    data = await request.body()
    print("------>", data)
    async def request_body():
        return {'type': 'http.request', 'body': data, 'more_body': False}
    request = Request(request.scope, request_body)

    response = await call_next(request)

    print("2222")
    process_time = time.time() - start_time
    print(process_time)
    response.headers["X-Process-Time"] = f"{process_time * 1000:.3f}ms"
    return response


@app.post("/hi")
def home(data: dict = Body(...), q: str = Query(...)):

    print("333")
    return {"hello": data, "query": q}


if __name__ == '__main__':
    # run("app:app", port=8888, reload=True)
    run("main:app", port=8000, reload=True)
