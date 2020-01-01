# -*- coding: utf-8 -*-

'''
zhouzhongqing
2020年01月01日16:13:06
下载m3u8
'''

import requests
import sys, getopt

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


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


def write_file(r):
    with open("/home/zzq/temp/demo3.m3u8", "wb") as code:
        code.write(r.content)




if __name__ == '__main__':
    print("start")

    url = "https://cn7.kankia.com/hls/20191231/618724d74eb29a8c53ebd37254e81f10/1577758490/index.m3u8"
    res = requests.get(url, headers=headers, timeout=999)
    print(res.status_code)
    write_file(res)
    print("end")
