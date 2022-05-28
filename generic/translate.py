# -*- coding: utf-8 -*-

'''
zhouzhongqing
2022年5月18日14:36:40
翻译

pip install keyboard
pip install requests
'''
import requests
import json

import time
# import pandas as pd # pandas也有获取剪贴板api，好像有格式
import pyperclip
import keyboard
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(1)

# 上次翻译内容
prev_content = ''

keyboard_count = 0
# 最大失败次数
max_fail_count = 2;

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

proxies = {
    "http": "http://pc-cd-356:1080",
    'https': 'http://pc-cd-356:1080'
}


def youdao_api(keyword):
    '''
    有道翻译
    @param keyword
    '''
    try:
        api = 'http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i=' + keyword
        res = requests.get(api, headers=headers, timeout=20)
        # print(res.text)
        translateResult = json.loads(res.text)['translateResult']
        for items in translateResult:
            for item in items:
                print(item['src'])
                print(item['tgt'])
    except BaseException as ex:
        print('出现错误: ')
        print(ex)
        raise RuntimeError('有道翻译失败了')
    finally:
        print("\n--------------------------------")


def google_api(keyword):
    '''
    谷歌翻译
    @param keyword
    '''
    try:
        api = 'https://translate.google.cn/translate_a/single?client=gtx&dt=t&dj=1&ie=UTF-8&sl=auto&tl=zh-CN&q=' + keyword
        res = requests.get(api, headers=headers, proxies=proxies, timeout=20)
        # print(res.text)
        sentences = json.loads(res.text)['sentences']
        for item in sentences:
            print(item['orig'])
            print(item['trans'])
    except BaseException as ex:
        print('出现错误: ')
        print(ex)
        raise RuntimeError('谷歌翻译失败了')
    finally:
        print("\n--------------------------------")


def start_translate(count):
    '''
    开始翻译
    @param count
    '''
    # clipboard = pd.read_clipboard()
    clipboard = pyperclip.paste()
    # print(clipboard)
    # google_api(clipboard)
    #    google_api(
    #       'Extends the Spring programming model to support the well-known Enterprise Integration Patterns. Spring Integration enables lightweight messaging within Spring-based applications and supports integration with external systems via declarative adapters. ')
    global prev_content
    if prev_content != clipboard:
        # print('开始翻译：' + clipboard + '\n')
        # 上次翻译的内容和剪贴板不一致，才调用翻译接口
        try:
            if selected_api == '0':
                youdao_api(clipboard)
            elif selected_api == '1':
                google_api(clipboard)
            else:
                youdao_api(clipboard)
            prev_content = clipboard
        except BaseException as ex:
            print(ex)
            translate_count = count + 1
            if translate_count < max_fail_count:
                # 如果失败了，重新调用
                start_translate(translate_count)
            else:
                print('已经到达最大重试：' + str(translate_count) + '次 ' + clipboard)


def keyboard_listener():
    keyboard.add_hotkey('ctrl+right', start_translate, args=(0,))
    # Block forever, like `while True`.
    keyboard.wait()


if __name__ == '__main__':
    print('start')
    selected_api = input('请选择翻译接口 0-有道 1-谷歌,默认有道 ')
    keyboard_listener()
    print('end')
