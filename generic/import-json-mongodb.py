# -*- coding: utf-8 -*-
'''
zzq
导入json到mongodb
2020年10月9日08:56:39
'''
import sys
import os
#mongoimport -u root -p xxx  --db game_server --collection game_ip_list_config --file game_ip_list_config.json
COMMAND_TEMPLATE = "%s    --db %s --collection %s --file %s"
def command_list(command_path,db_name,folder_path):
    command_list = []
    if os.path.exists(folder_path):
        for item in os.listdir(folder_path):
            command = COMMAND_TEMPLATE % (command_path,db_name,item.replace(".json",""),folder_path + item);
            #print(command)
            command_list.append(command)
    return command_list;

if __name__ == '__main__':
    command_path = None;
    folder_path = None;
    db_name = None
    # command_path = "D:/software/MongoDB/Server/4.0/bin/mongoimport.exe";
    # db_name = "mm_video"
    # folder_path = "C:/Users/Administrator/Desktop/mm_video/mm_video/";
    if len(sys.argv) > 1:
        command_path = sys.argv[1];

    if len(sys.argv) > 2:
        db_name = sys.argv[2];

    if len(sys.argv) > 3:
        folder_path = sys.argv[3];

    if db_name:
        if command_path:
            if folder_path:
                all_command = command_list(command_path,db_name,folder_path)
                for item in all_command:
                    print(item)
                    os.system(item)
            else:
                print("文件夹路径不能为空")
        else:
            print("命令路径不能为空")
    else:
        print("db名称不能为空")
