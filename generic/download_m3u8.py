# -*- coding: utf-8 -*-

'''
zhouzhongqing
2020年01月01日16:13:06
下载m3u8
'''

import requests
import sys, getopt
from concurrent.futures import ThreadPoolExecutor

import os

import time

pool = ThreadPoolExecutor(50)

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

prefix = "/home/zzq/temp/"


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('输入的文件为：', inputfile)
    print('输出的文件为：', outputfile)


def download(url):
    r = requests.get(url)
    with open("/home/zzq/temp/demo3.m3u8", "wb") as code:
        code.write(r.content)


def write_file(r, file_path):
    file_path = file_path.replace("//", "/").strip()
    with open(file_path, "wb") as code:
        code.write(r.content)
    return file_path;


def create_folder(path):
    if os.path.exists(path) == False:
        print("makedirs " + path)
        os.makedirs(path)




def parse_m3u8(url, file_path):
    res = requests.get(url, headers=headers, timeout=999)
    print(res.status_code)
    if 200 == res.status_code:
        path = write_file(res, file_path)
        download_file_list = []
        f = open(path)  # 返回一个文件对象
        line = f.readline()  # 调用文件的 readline()方法
        while line:
            # print(line)
            if line is not None:
                if line.rfind(".m3u8") >= 0 or line.rfind(".ts") >= 0:
                    download_file_list.append(line)
            line = f.readline()

        # 选择前缀
        suffix = url[url.find("://") + 3:len(url)]
        host = url[0:url.find("://") + 3] + suffix.split("/")[0] + "/"
        url_arr = url.split("/")
        full_prefix = url.replace(url_arr[len(url_arr) - 1], "")
        print(full_prefix)
        print(host)

        option_prefix = "";
        if len(download_file_list) > 0:
            #选择下载文件的前缀
            if download_file_list[0][0:1] == "/":
                option_prefix = host;
            else:
                res = requests.get(host + download_file_list[0], headers=headers, timeout=999)
                if 200 == res.status_code:
                    option_prefix = host;
                else:
                    res = requests.get(full_prefix + download_file_list[0], headers=headers, timeout=999)
                    if 200 == res.status_code:
                        option_prefix = full_prefix

        print("option_prefix " + option_prefix)

        for item in download_file_list:
            #print("downloading " + option_prefix + item)
            item_arr = item.split("/")
            item_full_prefix = item.replace(item_arr[len(item_arr) - 1], "")
            item_mkdir_path = prefix + item_full_prefix
            create_folder(item_mkdir_path)
            if item.rfind(".ts"):
                pool.submit(download_ts_file, option_prefix + item,prefix + item)
            elif item.rfind(".m3u8"):
                parse_m3u8(option_prefix +  item,item_mkdir_path)

def download_ts_file(url,item_save_path):
    res = requests.get(url, headers=headers, timeout=999)
    if 200 == res.status_code:
        write_file(res,item_save_path)
        print("%s download successful" % url.strip())


if __name__ == '__main__':
    print("start")
    start_time = time.time()
    url = "https://cn7.kankia.com/hls/20191231/618724d74eb29a8c53ebd37254e81f10/1577758490/index.m3u8"
    if len(sys.argv) > 1:
        url = sys.argv[1]

    if len(sys.argv) > 2:
        prefix = sys.argv[2]

    file_name_suffix = url[url.rfind("/"):len(url)]
    parse_m3u8(url, prefix + file_name_suffix)
    end_time = time.time()
    print("take up time %d " % (end_time - start_time) )
    print("end")
