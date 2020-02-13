# -*- coding: utf-8 -*-

import sys
import subprocess
import os
import jieba
import datetime
import requests
import re

'''
可重试的axel
zhouzhongqing
2020年02月10日12:38:43

测试
python axel-try.py -n 10 -o . http://117.128.6.23/cache/mirror.as29550.net/releases.ubuntu.com/18.04.3/ubuntu-18.04.3-desktop-amd64.iso?ich_args2=465-10134506061282_14764238c99abf515215503101984ce3_10001002_9c896c2dd4c2f2d49333518939a83798_0c0caa8f3617d12916b5a1decd43b462
python axel-try.py -n 10 -o . https://img-blog.csdnimg.cn/20200210111658880.png
python axel-try.py -n 10 -o . https://archive.apache.org/dist/maven/binaries/apache-maven-3.0.1-bin.tar.gz
'''



#文件长度
content_length = 0

success_list = ["用时"]
#是url的标记
url_tags = ['https://','http://','ftp://']

thread_number = 0
# execute command, and return the output
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text

def cmd(command):
    # res = subprocess.run(command, stdout=subprocess.PIPE )
    # print('---------------------------------------------------- ')
    # return_str = str(res.stdout, encoding='utf-8');
    # res_list = list(jieba.cut(return_str))
    # print(res_list)
    #
    # judge_success = False
    # for item in success_list:
    #     if item in res_list:
    #         judge_success = True
    #         break
    #
    # if judge_success:
    #     print("恭喜您下载成功!")
    # else:
    #     print("下载失败!正在重试......" + str(datetime.datetime.now()) )
    #     cmd(command)



    # os.system(command)
    # print('-----------------------开始下载----------------------------- ')
    # res = execCmd(command)
    # print('res ' + res)



    print('-----------------------开始下载----------------------------- ')
    tips = []
    # 最多保存多少行数据
    max_tips = 20
    for i in range(0, max_tips):
        tips.append('')
    index = 0
    subp = subprocess.Popen(command, stdout=subprocess.PIPE)
    while subp.poll() is None:
        text = str(subp.stdout.readline(), encoding='utf=8')
        tips[index] = text
        index = index + 1
        if index >= max_tips:
            #重置
            index = 0
        print(" %s" % text)



    # res_list = list(jieba.cut(''.join(tips)))
    # index = 0
    # #增加大小
    # #success_list.append(content_length)
    # for item in success_list:
    #     if item in res_list:
    #        index = index + 1
    #
    # if index > 0:
    #     print('下载成功了')
    # else:
    #     print("下载失败!正在重试......" + str(datetime.datetime.now()))
    #     cmd(command)


    print('-----------------------开始检查完整性----------------------------- ')
    index = 0
    try:
        output = subprocess.check_output(command,shell=False)
    except Exception as e:
        #Command '['axel', '-o', '.', 'https://img-blog.csdnimg.cn/20200210111658880.png']' returned non-zero exit status 1
        import traceback
        #traceback.print_exc()  # 打印异常信息
        exc_type, exc_value, exc_traceback = sys.exc_info()
        error = str(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))  # 将异常信息转为字符串
        #print(error)
        if error.find('returned non-zero exit status'):
           index = 1
           print("returned non-zero exit status 没有状态文件，无法继续下载")
    finally:
        if index > 0:
            print('下载成功了')
        else:
            print("下载失败!正在重试......" + str(datetime.datetime.now()))
            cmd(command)





if __name__ == '__main__':
    print('start')


    #测试代码
    # try:
    #     #url = "https://img-blog.csdnimg.cn/20200210111658880.png"
    #     url = "https://liquidtelecom.dl.sourceforge.net/project/generic-software/php/openresty-1.15.8.2.tar.gz"
    #     output = subprocess.check_output(["axel",'-o' ,'.', url],shell=False)
    #     print('asd' + str(output,encoding='utf-8'))
    # except Exception as e:
    #     #Command '['axel', '-o', '.', 'https://img-blog.csdnimg.cn/20200210111658880.png']' returned non-zero exit status 1
    #     import traceback
    #     #traceback.print_exc()  # 打印异常信息
    #     exc_type, exc_value, exc_traceback = sys.exc_info()
    #     error = str(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))  # 将异常信息转为字符串
    #     print(error)
    #     if error.find('returned non-zero exit status'):
    #        print("没有状态文件，无法继续下载")


    if len(sys.argv) > 1:
        command_str = 'axel '
        command = ['axel']
        url = ''
        file_prefix = './'
        file_path_index = -1
        thread_index = -1
        for index, item in enumerate(sys.argv):
            if index > 0:
                command.append(item)
                command_str += ' ' + item
                #寻找-o
                if "-o" == item:
                    file_path_index = index + 1
                # 寻找-n
                if "-n" == item:
                    thread_index = index + 1
                for url_item in url_tags:
                    if item.find(url_item) >= 0:
                        url = item


        # if file_path_index > -1:
        #     file_prefix = sys.argv[file_path_index]
        #     if file_prefix == ".":
        #        file_prefix = "./"

        # response = requests.get(url, timeout=999)
        # content_length = dict(response.headers)['Content-Length']
        # print('文件大小 %s ' % content_length)
        #
        # url_temp = url
        # if url_temp.rfind('?') >= 0:
        #     url_temp = url_temp[url_temp.rfind("?")+1:len(url_temp)]
        # file_size = os.path.getsize(file_prefix + url_temp[url_temp.rfind('/')+1:len(url_temp)])
        # print("本地文件: " + str(file_size))
        # if str(file_size) != content_length:
        #     print(command_str)
        #     cmd(command)
        # else:
        #     print('文件已经下载完成!')
        print(command_str)
        cmd(command)
    else:
        print("请输入axel参数!")
    print('end')
