# _*_ coding:utf-8 _*_
"""
@Time: 2022/8/30 21:54
@Author: lijian
@Des： 测试文件
"""
# import traceback

# from logging import getLogger
#
#
# logger = getLogger(__name__)
# try:
#     a = 1 / 0
#
# except ZeroDivisionError as e:
#     logger.error("除以零？", exc_info=True)



# try:
#     a =10
#     ss
# except Exception :
#     exc_msg = '\n' + "-" * 40 + "  catch some exceptions  " + "-" * 40 + '\n'
#     exc_msg += traceback.format_exc()+'\n'
#     local_vars = locals()
#     del local_vars['exc_msg']
#     exc_msg +=f"{local_vars}" + '\n'
#     exc_msg += "_" *100
#     print(exc_msg)

a = {"username": "li"}
a.update({"passwprd":123})


print(a)