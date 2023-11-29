# -*- coding: utf-8 -*-

import os
import time
import random

def device():
    os.system("adb devices")

def swiper(addr):
    # 该整数位于闭区间[a, b]之间，包括a和b
    time.sleep(5.20)
    print("执行滑动")
    os.system(" adb -s "+ addr +" shell input swipe 100 900 100 450")
if __name__ == '__main__':
    device()
    addr = input("请输入地址")
    print("输入的地址是 " + addr)
    while True:
        swiper(addr)