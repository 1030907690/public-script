# -*- coding: utf-8 -*-

'''
zhouzhongqing
2022年5月18日14:36:40
翻译
'''
import requests
import json

import time
# import pandas as pd # pandas也有获取剪贴板api，好像有格式
import pyperclip

# 上次翻译内容
prev_content = ''

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

proxies = {
    "http": "http://pc-cd-356:1080",
    'https': 'http://pc-cd-356:1080'
}


def youdao_api(keyword):
    try:
        api = 'http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i=' + keyword
        res = requests.get(api, headers=headers,timeout=20)
        # print(res.text)
        translateResult = json.loads(res.text)['translateResult']
        for items in translateResult:
            for item in items:
                print(item['src'])
                print(item['tgt'])
    except BaseException as ex:
        print('出现错误: ')
        print(ex)
    print("\n--------------------------------")


def google_api(keyword):
    try:
        api = 'https://translate.google.cn/translate_a/single?client=gtx&dt=t&dj=1&ie=UTF-8&sl=auto&tl=zh-CN&q=' + keyword
        res = requests.get(api, headers=headers, proxies=proxies,timeout=20)
        # print(res.text)
        sentences = json.loads(res.text)['sentences']
        for item in sentences:
            print(item['orig'])
            print(item['trans'])
    except BaseException as ex:
        print('出现错误: ')
        print(ex)
    print("\n--------------------------------")


if __name__ == '__main__':
    print('start')

    selected_api = input('请选择翻译接口 0-有道 1-谷歌,默认有道 ')

    while True:
        time.sleep(1)
        # clipboard = pd.read_clipboard()
        clipboard = pyperclip.paste()
        # print(clipboard)
        # google_api(clipboard)
        #    google_api(
        #       'Extends the Spring programming model to support the well-known Enterprise Integration Patterns. Spring Integration enables lightweight messaging within Spring-based applications and supports integration with external systems via declarative adapters. ')
        if prev_content != clipboard:
            # 上次翻译的内容和剪贴板不一致，才调用翻译接口
            if selected_api  == '0':
                youdao_api(clipboard)
            elif selected_api == '1':
                google_api(clipboard)
            else:
                youdao_api(clipboard)
            prev_content = clipboard
    print('end')
