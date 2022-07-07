# -*-coding: UTF-8 -*-

'''
@author Zhou Zhongqing
2022年7月7日11:22:31
下载模块加速
'''
import os

if __name__ == '__main__':
    while True:
        module = input("enter module,please ？")
        os.system("pip3 install  " + module + " -i https://mirrors.aliyun.com/pypi/simple/");
