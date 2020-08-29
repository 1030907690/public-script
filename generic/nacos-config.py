# -*-coding: UTF-8 -*-

'''
@author zhouzhongqing
seate配置导入到nacos
2020年8月29日09:36:25
'''
import sys
import http.client
import os


if __name__ == '__main__':
    headers = {
        'content-type': "application/x-www-form-urlencoded"
    }
    hasError = False
    file_name = 'config.txt'
    if os.path.exists(file_name):
        for line in open(file_name):
            pair = line.split('=')
            if len(pair) < 2:
                continue
            print(line),
            url_prefix = sys.argv[1]
            conn = http.client.HTTPConnection(url_prefix)
            if len(sys.argv) == 3:
                namespace = sys.argv[2]
                url_postfix = '/nacos/v1/cs/configs?dataId={0}&group=SEATA_GROUP&content={1}&tenant={2}'.format(
                    str(pair[0]), str(line[line.index('=') + 1:]).strip(), namespace)
            else:
                url_postfix = '/nacos/v1/cs/configs?dataId={}&group=SEATA_GROUP&content={}'.format(str(pair[0]), str(
                    line[line.index('=') + 1:])).strip()
            conn.request("POST", url_postfix, headers=headers)
            res = conn.getresponse()
            data = res.read()
            if data.decode("utf-8") != "true":
                hasError = True
        if hasError:
            print("init nacos config fail.")
        else:
            print("init nacos config finished, please start seata-server.")
    else:
        print(os.getcwd() + "/" + file_name + " not found. ")
    input('Enter any key to end')
