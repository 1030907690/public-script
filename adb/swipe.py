# -*- coding: utf-8 -*-

import os
import time
import random

import keyboard
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(1)
# 热键
hot_keyboard = 'ctrl+alt+f1'

# 翻译开关 0 关闭  1 开启
enable = 0


def device():
    os.system("adb devices")


def swiper(addr):
    if enable == 1:
        print("执行滑动")
        os.system(" adb -s " + addr[0] + " shell input swipe 100 900 100 450")


def keyboard_tips():
    '''
    提示
    '''
    global enable
    # 异或切换   0 ^ 1 = 1 , 1 ^ 1 = 0
    enable = enable ^ 1
    if enable == 0:
        print('已关闭')
    elif enable == 1:
        print('已开启')


def keyboard_listener(addr):
    keyboard.add_hotkey(hot_keyboard, keyboard_tips, args=())
    pool.submit(start, (addr,))
    # Block forever, like `while True`.
    keyboard.wait()


def start(addr):
    while True:
        swiper(addr)
        # 该整数位于闭区间[a, b]之间，包括a和b
        time.sleep(random.randint(3, 6))


if __name__ == '__main__':
    device()
    addr = input("请输入地址")
    print("输入的地址是 " + addr)
    keyboard_listener(addr)
