import logging
import sys
from types import FrameType
from typing import cast

import uvicorn
from fastapi import FastAPI
from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
                level, record.getMessage(), )


loguru_config = {
    "handlers": [
        {
            "sink": sys.stdout,
            "level": "DEBUG",
            "format": "<green>{time:YYYY-mm-dd HH:mm:ss.SSS}</green> | {thread.name} | <level>{level}</level> | "
                      "<cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
            },
        {
            "sink": 'fastapi.log',
            "level": "DEBUG",
            "rotation": "10 MB",
            "retention": "1 week",
            "encoding": 'utf-8',
            "format": "{time:YYYY-mm-dd HH:mm:ss.SSS} | {thread.name} | {level} | {module} : {function}:{line} -  {"
                      "message}"
            },
        {
            "sink": 'fastapi-error.log',
            "serialize": True,
            "level": 'ERROR',
            "retention": "1 week",
            "rotation": "10 MB",
            "encoding": 'utf-8',
            "format": "{time:YYYY-mm-dd HH:mm:ss.SSS} | {thread.name} | {level} | {module} : {function}:{line} -  {"
                      "message}"
            },
        ],
    }

# 需要替换的日志器名称
LOGGER_NAMES = ("uvicorn", "uvicorn.access",)


# 如果发现日志重复输出问题，请注意各个日志器的 propagate 属性

# 获取当前所有日志器名称的方法
# logger_name_list = [name for name in logging.root.manager.loggerDict]
# print("logger_name_list", logger_name_list)


def init_logger():
    for logger_name in LOGGER_NAMES:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler()]
    logger.configure(**loguru_config)


app = FastAPI()


@app.get('/')
def home():
    return {"hello", "world"}


if __name__ == '__main__':
    config = uvicorn.Config("temp:app")
    server = uvicorn.Server(config)
    init_logger()
    server.run()
