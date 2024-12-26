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
        addr_str = addr[0]
        array = addr_str.split(",")
        for item in array:
            ran_x_num = random.randint(0, 10)
            ran_y_num = random.randint(0, 10)
            x1, y1, x2, y2 = 100 - ran_x_num, 900 - ran_y_num, 100 - ran_x_num, 450 - ran_y_num
            cmd = " adb -s " + item + " shell input swipe " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2)
            print("执行滑动 " + cmd)
            os.system(cmd)


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
        time.sleep(random.randint(10, 50))


if __name__ == '__main__':
    device()
    addr = input("请输入地址,多个英文逗号分开")
    print("输入的地址是 " + addr)
    keyboard_listener(addr)
