'''
模拟键盘输入
2025-10-28 15:16:00
Zhou Zhongqing

经过测试pynput 比较快
'''
# import pydirectinput
import time
# import pyautogui

from pynput.keyboard import Key, Controller
# import keyboard as kb

import sys
import getopt


def pynput_input(sleep, str: str):  # 执行时间0.007
    if sleep > 0:
        time.sleep(sleep)
    keyboard = Controller()

    str_array: [str] = list(str)
    for key in str_array:
        keyboard.press(key)
        time.sleep(0.01)

    keyboard.press(Key.enter)


# def keyboard_input():  # 执行时间 0.183
#     time.sleep(3)
#     sn = [1, 1, 2, 0, 5, 2, 3, 2]
#     for key in sn:
#         kb.press_and_release(str(key))


def help():
    print('''
    -t --time time second, optional
    -s --str send str,must
    ''')


if __name__ == '__main__':
    # longopts 表示识别--help, --host=xx, --port=1234的长选项
    opts, args = getopt.getopt(sys.argv[1:], "t:s:", ["help", "time=", "str="])

    sleep_time = 0
    send_str = None

    if opts is None or len(opts) < 1:
        help()

    for opt, arg in opts:
        if opt in ("-help", "--help"):
            help()
        elif opt in ("-t", "--time"):
            sleep_time = int(arg)
        elif opt in ("-s", "--str"):
            send_str = arg
        else:
            help()

    if send_str:
        start_time = time.time()
        pynput_input(sleep_time, send_str)
        end_time = time.time()
        diff_time = (end_time - start_time) * 1000
        print(f"执行时间{diff_time}毫秒")
