# -*- coding: utf-8 -*-

'''
测试服上传热更的代码
'''

import paramiko
import os
import time

host = "47.114.147.81";
user_name = "root";
password = "root";


class FileInfo:
    path = '';
    update_time = '';

    def __init__(self, path, update_time):
        self.path = path
        self.update_time = update_time


def createConnection():
    #1、密码连接
    # ssh = paramiko.SSHClient()
    # # 自动认证
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(host, 22, user_name, password);

    #2、密钥连接

    private_key = paramiko.RSAKey.from_private_key_file('/home/zzq/work/docs/server-ssh/app-dabaitu/id_rsa')

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=host, port=22, username="root", pkey=private_key)

    return ssh;


# os.path.getatime(file) 输出文件访问时间
# os.path.getctime(file) 输出文件的创建时间
# os.path.getmtime(file) 输出文件最近修改时间
def fileTime(file):
    return [time.ctime(os.path.getatime(file)), time.ctime(os.path.getctime(file)), time.ctime(os.path.getmtime(file))]


def list_file(path, all_file):
    for file_item in os.listdir(path):
        if os.path.isdir(path + file_item):
            list_file(path + file_item + "/",all_file)
        elif os.path.isfile(path + file_item):
            # print(file_item)
            file_info = FileInfo(path + file_item, fileTime(path + file_item)[2])
            all_file.append(file_info)
            #print(file_item + "--" + fileTime(path + file_item)[2])


if __name__ == '__main__':
    print("start");
    ssh = createConnection();
    #BASE_PATH = "F:/work/self/public-script/lua/conf/";
    #TARGET_PATH = "/usr/local/openresty/nginx/conf/";
    BASE_PATH = "/home/zzq/work/self/public-script/ssh/script/";
    TARGET_PATH = "/home/new_project/script/";


    # 确定要上传的文件
    upload_file_list_file = [];

    all_file_dict = {}

    while True:
        all_file = []
        list_file(BASE_PATH, all_file)
        for item in all_file:
            #print(item.path + "--" + item.update_time)
            if  item.path in all_file_dict.keys():
                #print("存在")
                if item.update_time != all_file_dict[item.path]:
                    print("update " + item.path)
                    #覆盖
                    all_file_dict[item.path] = item.update_time
                    #加入更新列表
                    upload_file_list_file.append(item.path)
            else:
                #print("不存在")
                #新增
                all_file_dict[item.path] = item.update_time
                # 加入更新列表
                upload_file_list_file.append(item.path)

        # 删除、上传文件
        # 实例化一个 sftp对象,指定连接的通道
        sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
        for file_item in upload_file_list_file:
            # 发送文件
            print("put file " + file_item + " target " + (
                file_item.replace(BASE_PATH, TARGET_PATH)))
            sftp.put(localpath=file_item, remotepath=file_item.replace(BASE_PATH, TARGET_PATH));
        time.sleep(2)
        upload_file_list_file = []






    sftp.close()
    ssh.close();
    print("end");
    # random_input = input(" 请输入任意字符结束. ");
