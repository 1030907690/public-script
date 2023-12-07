# -*- coding: utf-8 -*-


import socket

import os
import threading

port_start = 0
port_end = 65536  # 65535   + 1

live_ips = []

all_live_addr = []


# ip 是否能ping通
def ping_ip(ip_str):
    cmd = ["ping", "-n", "1", ip_str]
    output = os.popen(" ".join(cmd)).readlines()
    for line in output:
        if str(line).upper().find("TTL") >= 0:
            print("ip: %s is ok " % ip_str)
            live_ips.append(ip_str)
            break


def find_ip(ip_prefix):
    '''''
    给出当前的192.168.0 ，然后扫描整个段所有地址
    '''
    threads = []
    for i in range(1, 256):
        ip = '%s.%s' % (ip_prefix, i)
        threads.append(threading.Thread(target=ping_ip, args={ip, }))
    for i in threads:
        i.start()
    for i in threads:
        i.join()


def scan(ip_str):
    # print(ip_str)
    for port in range(port_start, port_end):
        if check_port(ip_str, port):
            all_live_addr.append(ip_str + ":" + str(port))
        else:
            print(ip_str + " " + str(port) + ' 端口不通')


def check_port(ip, port):
    print("检测 %s:%d" % (ip, port))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"错误: {str(e)}")
    finally:
        sock.close()


def scan_port():
    threads = []
    for live_ip in live_ips:
        threads.append(threading.Thread(target=scan, args={live_ip, }))
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print('执行结束...')


def adb_connect():
    for ip_addr in all_live_addr:
        cmd = ["adb", "connect", ip_addr]
        output = os.popen(" ".join(cmd)).readlines()
        for line in output:
            print(line)


if __name__ == '__main__':
    find_ip('192.168.3')
    find_ip('192.168.24')
    # live_ips.append("192.168.3.54")
    print(live_ips)
    scan_port()
    print(all_live_addr)
    adb_connect()
