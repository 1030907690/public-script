# -*- coding: utf-8 -*-
'''
分析占用
'''

import os
import sys


from decimal import Decimal, getcontext

def get_folder_size(folder_path):
    total_size = 0
    errors = []
    for folder_name, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(folder_name, filename)
            try:
                total_size += os.path.getsize(file_path)
            except FileNotFoundError as e:
                errors.append(e)
    return total_size




if __name__ == '__main__':
    getcontext().prec = 2
    folder_path = 'D:/software'
    input_path = sys.argv[1]
    if input_path:
        folder_path = input_path

    gb_files = []
    for item_path in os.listdir(folder_path):
        full_path = folder_path +"/"+ item_path
        size = get_folder_size(full_path)
        mb = Decimal(size) / Decimal(1024) / Decimal(1024)
        if mb > 100:
            gb = Decimal(mb) / Decimal(1024)
            print(f"{full_path} 文件或文件夹大小为 {gb}GB")
            gb_files.append({"path":full_path,"size":gb})
        else:
            print(f"{full_path} 文件或文件夹大小为 {mb}MB")


    print("GB文件或文件夹")
    if gb_files and len(gb_files) > 0:
        sorted_list = sorted(gb_files, key=lambda x: x['size'])  # 根据元组的第二个元素排序
        for gb in sorted_list:
            print(f"{gb['path']} 文件或文件夹大小为 {gb['size']}GB")