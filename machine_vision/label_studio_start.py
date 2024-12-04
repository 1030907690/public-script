# -*- coding: utf-8 -*-

import time
import random

import pydirectinput



actions = [
    "conda activate label",
    "label-studio start"
]
def call_cmd_box():
    time.sleep(1)
    pydirectinput.click(10, 1080)  # 移动鼠标至坐标200，220，并点击左键
    pydirectinput.write('cmd')
    pydirectinput.press('enter')
    pydirectinput.press('enter')



def keyboard_input(arg):
    # 该整数位于闭区间[a, b]之间，包括a和b
    time.sleep(random.randint(2, 4))
    action = actions[int(arg)]

    pydirectinput.write(action)

    pydirectinput.press("enter")




if __name__ == '__main__':
    call_cmd_box()
    keyboard_input(0)
    keyboard_input(1)
    input("输入任意键结束")
