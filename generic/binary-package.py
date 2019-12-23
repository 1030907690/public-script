# -*- coding: utf-8 -*-
'''
zhouzhongqing
2019年12月23日20:49:37
打包成二进制可执行文件
'''

'''
打包单个exe文件
-F 选项可以打出一个exe文件，默认是 -D，意思是打成一个文件夹。
pyinstaller -F TestDataGen.py
打出的桌面程序去掉命令行黑框 -w 选项可以打桌面程序，去掉命令行黑框
pyinstaller -F -w TestDataGen.py
修改程序默认图标 -i 可以设置图标路径，将图标放在根目录：
pyinstaller -F -w -i gen.ico TestDataGen.py
'''


import sys

import os


if __name__ == '__main__':
    os.system("pip3.5 install  PyInstaller   -i https://pypi.tuna.tsinghua.edu.cn/simple/")
    file = sys.argv[1]
    os.system("pyinstaller -F  %s " % file)



