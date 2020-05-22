# -*- coding: utf-8 -*-
'''
zzq
重连WiFi
2020年5月22日23:56:24
'''
import subprocess
import time
import os
from time import strftime, localtime

ssid = "ChinaNet-efCC"


def reconnect():
    '''
    重连
    '''
    print("%s 正在重连WiFi" % strftime("%Y-%m-%d %H:%M:%S", localtime()))
    os.system("netsh wlan disconnect")
    os.system("netsh wlan connect ssid=%s name=%s" % (ssid, ssid))


def check_wifi():
    sleep = 2;
    subp = subprocess.Popen("ping baidu.com -t", stdout=subprocess.PIPE)
    while subp.poll() is None:
        text = str(subp.stdout.readline(), encoding='utf=8')
        print(" %s" % text)
        if match(text):
            reconnect()
            break
        time.sleep(sleep)


def match(text):
    '''
    匹配
    '''
    # 如果匹配到failure就认为是没网了   我这系统是英文版  其他的可以改下匹配规则
    if text:
        if text.find('failure') >= 0 or text.find('could not find host') >= 0:
            return True
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    while True:
        check_wifi()
        time.sleep(30)
