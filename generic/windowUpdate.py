# -*- coding: utf-8 -*-
'''
zzq
关闭windows update
2021年11月27日20:01:29
'''
import subprocess
import time
import os
from time import strftime, localtime




if __name__ == '__main__':
    while True:
        os.system("net stop wuauserv")
        os.system("net stop WaaSMedicSvc")
        time.sleep(10)
