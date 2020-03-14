# -*- coding: utf-8 -*-

'''
zhouzhongqing
2019年11月5日18:30:30
ssr帐号更新
'''

import os
import requests
from bs4 import BeautifulSoup
import base64
import re
import platform


# 写入文件
def write_to_file(file_name, txt):
    '''''
        讲txt文本存入到file_name文件中
    '''
    print("正在存储文件" + str(file_name));
    # 1 打开文件
    # w 如果没有这个文件将创建这个文件
    '''
    'r'：读

    'w'：写

    'a'：追加

    'r+' == r+w（可读可写，文件若不存在就报错(IOError)）

    'w+' == w+r（可读可写，文件若不存在就创建）

    'a+' ==a+r（可追加可写，文件若不存在就创建）
    '''
    f = open(file_name, 'a+', encoding='utf-8');
    # 2 读写文件
    f.write(str(txt));
    # 3 关闭文件
    f.close();


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


def ssr_account1():
    ssr_domain = "https://github.com/Alvin9999/pac2/blob/master/ssconfig.txt";

    try:
        content_string = "";
        content = requests.get(ssr_domain, headers=headers, timeout=999);
        # print(content.status_code)
        if content.status_code == 200:
            # print(content.text)
            # 初始化并制定解析器
            soup = BeautifulSoup(content.text, "lxml");
            tableContent = soup.find_all(class_='highlight tab-size js-file-line-container');
            # print(tableContent)
            for item in tableContent[0]:
                if item is not None and str(item).strip() != "":
                    # print(item)
                    # print(item.text);
                    # content_string += str(item.text).replace("\n","")+"\n";
                    content_string += str(item.text).replace("\n", "");

                    # if os.path.exists("ssconfig.txt"):
                    #  os.remove("ssconfig.txt")
            # write_to_file("ssconfig.txt",content_string);
            ssr_info = str(base64.b64decode(content_string),
                           encoding='utf-8')  # .replace("\n", "").replace("\t", "").replace("\r", "");
            print(ssr_info)
        else:
            print("访问ssr帐号失败!")

    except Exception as e:
        print("program error %s " % e)
    finally:
        print(" ")


def ssr_account2():
    try:
        content = requests.get("https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7",
                               headers=headers, timeout=999)
        if content.status_code == 200:
            # print(content.text)
            # 初始化并制定解析器
            soup = BeautifulSoup(content.text, "lxml");
            div = soup.select("div[class='markdown-body']");
            for div_item in div:
                p_list = div_item.find_all("p")
                for p_item in p_list:
                    # print(p_item.text+"--")
                    server_ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', p_item.text)
                    if server_ip:
                        # print(server_ip[0])
                        print(p_item.text)

                    if p_item.text.find("加密方式：") >= 0 or p_item.text.find("协议：") >= 0 or p_item.text.find("混淆：") >= 0:
                        print(p_item.text)
        else:
            print("访问失败!")

    except Exception as e:
        print(e)


def decode_base64(data):
    """Decode base64, padding being optional.
    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    return str(base64.b64decode(data),
               encoding='utf-8')


def ssr_account3():
    '''
    http://ss.pythonic.life/
    :return:
    '''
    ssr_account_domain_list = ["https://muma16fx.netlify.com/",
                               "https://qiaomenzhuanfx.netlify.com/",
                               "https://raw.githubusercontent.com/ssrsub/ssr/master/ssrsub",
                               "https://raw.githubusercontent.com/voken100g/AutoSSR/master/online",
                               "https://raw.githubusercontent.com/voken100g/AutoSSR/master/recent"
        , "https://youlianboshi.netlify.com/"
                               ]
    for ssr_doamin in ssr_account_domain_list:

        try:
            content = requests.get(ssr_doamin, headers=headers, timeout=999);
            # print(content.status_code)
            if content.status_code == 200:
                # print(content.text)
                data = content.text

                ssr_info = decode_base64(data)
                # ssr_info = str(base64.b64decode(content.text),  encoding='utf-8')
                print(ssr_info)
        except Exception as e:
            print("program error %s %s" % (e, ssr_doamin))
        finally:
            print()


def ssr_account4():
    domain_prefix = 'https://t1.free-air.org'
    try:
        content = requests.get(domain_prefix + '/ss%e5%85%8d%e8%b4%b9%e8%b4%a6%e5%8f%b7/',
                               headers=headers, timeout=999)
        if content.status_code == 200:
            # print(content.text)
            # 初始化并制定解析器
            soup = BeautifulSoup(content.text, "lxml");
            figure = soup.select("figure[class='wp-block-image']");
            image = figure[1].find('img')

            file_name = image['src'][image['src'].rfind('/'):len(image['src'])]
            res = requests.get(domain_prefix + image['src'], headers=headers, timeout=999)
            if 200 == res.status_code:
                write_file(res, os.getcwd() + file_name)
                print("%s download successful" % (os.getcwd() + file_name))

        else:
            print("访问失败!")

    except Exception as e:
        print(e)


def write_file(r, file_path):
    file_path = file_path.replace("//", "/").strip()
    with open(file_path, "wb") as code:
        code.write(r.content)
    return file_path;


if __name__ == '__main__':
    ssr_account1()
    ssr_account2()
    ssr_account3()
    ssr_account4()

    if platform.system() == "Windows":
        random = input("请按任意键退出")
