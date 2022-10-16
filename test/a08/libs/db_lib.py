# _*_ coding:utf-8 _*_
"""
@Time: 2022/9/21 22:05
@Author: lijian
@Des：  模拟数据库
"""
import json

from pathlib import Path

from typing import List
from pydantic import parse_file_as

from models8 import UserInDB

class FakeDB:
    def __init__(self):
        """
        1.拼接数据文件绝对路径
        2判断数据文件是否存在
        不存在：在内存中创建空数据文件
        存在：根据路径，读取到内存中  就是磁盘到内存

        """
        self.__data_path = Path(__file__).absolute().parent / "data.json"
        if not self.__data_path.exists():
            self.__data: List[UserInDB] = []
        else:
            #  接收文件路径，读取文件并将内容传递给parse_raw
            self.__data: List[UserInDB] = parse_file_as(List[UserInDB], self.__data_path)

    def all(self):
        """
        1.打印格式
        2，取出列表索引，取出列表每一个字典，根据索引打印内容
        :return:
        """
        print('-' * 35)
        print(f"{'No.':>3}{'username':>15}{'password':>15}")
        print('-' * 35)
        #  enumerate多用于在for循环中得到计数，利用它可以同时获得索引和值
        for i, user in enumerate(self.__data):
            print(f"{i:>3}{user.username:>15}{user.password:>15}")
            print('-' * 35)
        return self.__data

    def get_or_none(self, name):
        """
        1.循环判断字典是否存在这个用户
        :param name:
        :return:
        """
        for user in self.__data:
            if user.username == name:
                if user.username == name:
                    return user
        return None

    def save(self, user):
        if self.get_or_none(name=user.username) is not None:
            raise ValueError(f"不满足唯一性约束，当前用户名: {user.username}")
        self.__data.append(user)
        # print(self.__data)
        data = [x.dict() for x in self.__data]
        # print(data)
        # 以文本模式打开指向的文件，写入data，然后关闭文件
        self.__data_path.write_text(json.dumps(data, indent=4), encoding="utf-8")

db = FakeDB()

if __name__ == '__main__':

    db.all()
    # print(db.get_or_none("li"))
    #
    # db.save(UserInDB(username="lijian", password="123"))



