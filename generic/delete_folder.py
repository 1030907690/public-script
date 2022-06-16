# -*-coding: UTF-8 -*-

'''
Zhou Zhongqing
删除文件夹及里面全部文件
2022年6月16日09:11:59
'''
import os
import shutil


def del_folder(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i)  # 取文件绝对路径
        if os.path.exists(path_file):
            if os.path.isfile(path_file):
                os.remove(path_file);
                print("remove " + path_file);
            else:
                shutil.rmtree(path_file)  # 递归删除文件夹
                print("rmtree " + path_file);


if __name__ == '__main__':
    del_path = input("请输入路径?")
    while True:
        input('按任意键执行删除')
        del_folder(del_path)
