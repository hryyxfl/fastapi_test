# _*_ coding:utf-8 _*_
"""
@Time: 2022/10/13 15:57
@Author: lijian
@Des：  gui
"""
from gooey import Gooey, GooeyParser

@Gooey(program_name="简单实例")
def main():
    parser = GooeyParser(description="第一个实例")
    parser.add_argument("文件路径", widget="FileChooser")  # 文件选择框
    parser.add_argument("日期", widget="FileChooser")  # 日期选择框
    args = parser.parse_args()  #  接收界面传递的参数
    print(args)


if __name__ == '__main__':
    main()