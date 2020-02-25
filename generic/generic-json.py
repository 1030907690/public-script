# -*- coding: utf-8 -*-

'''
启动应用 2019年1月24日10:04:31
'''

import os
import time


# 执行的应用程序
class ApplicationRunTime:
#    def __init__(self, id, name, workDir, status, sort, sleep, command, remarks, date):
    def __init__(self, name, workDir, status, sort, sleep, command, remarks):
        #self.id = id;
        # 名称
        self.name = name;
        # 工作路径
        self.workDir = workDir;
        # status 1 启用  0 禁用
        self.status = status;
        # sort  排序 小到大
        self.sort = sort;
        # 执行后睡眠时间
        self.sleep = sleep;
        # 执行命令
        self.command = command;
        # 备注
        self.remarks = remarks;


    def getId(self):
        return self.id;

    def getWorkDir(self):
        return self.workDir;

    def getName(self):
        return self.name;

    def getStatus(self):
        return self.status;

    def getSort(self):
        return self.sort;

    def getSleep(self):
        return self.sleep;

    def getCommand(self):
        return self.command;

    def getRemarks(self):
        return self.remarks;

    def getDate(self):
        return self.date;

    def __lt__(self, other):  # override <操作符
        if self.sort < other.sort:
            return True
        return False

#
# host = '127.0.0.1';
#
# port = 3306;
# user = 'root';
# passwd = 'root';
# db = 'script';
# charset = 'UTF8'
FILE_NAME = "command.json"

def getApplicationList(application_name):

    # conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
    #                        charset=charset);
    # cur = conn.cursor();
    # sql = "SELECT id,name,work_dir ,status, sort,sleep,command,remarks,date FROM  application where 1=1 and status='1' and application_name = '" + application_name + "'  order by  sort asc";
    # cur.execute(sql);
    # # 获取所有记录列表
    # results = cur.fetchall();
    #
    # project_list = [];
    # for row in results:
    #     application = ApplicationRunTime(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]);
    #     project_list.append(application);
    # cur.close();
    # conn.close();

    project_list = []
    import sys
    file_suffix = sys.argv[0]
    file_prefix = ""
    if file_suffix.rfind("/") >= 0:
        if file_suffix[0:1] == "/":
            file_prefix = file_suffix[0:file_suffix.rfind("/")+1]
        else:
            file_prefix = os.getcwd() +"/"+ file_suffix[0:file_suffix.rfind("/")+1]
    else:
        file_prefix = os.getcwd()+"/"

    print("prefix" + file_prefix)
    if os.path.exists(file_prefix+FILE_NAME):
        file = open(file_prefix+FILE_NAME, 'r', encoding='utf-8')
        import json
        command_arr = json.loads(file.read())
        file.close()
        for item in command_arr:
            #
            filed_arr = ["name","workDir","status","sort","sleep","command","remarks"]
            application = ApplicationRunTime(item[filed_arr[0]], item[filed_arr[1]], item[filed_arr[2]], item[filed_arr[3]], item[filed_arr[4]], item[filed_arr[5]], item[filed_arr[6]]);
            project_list.append(application);
    else:
        print("%s 不存在" % FILE_NAME)
    return project_list;


if __name__ == '__main__':
    print(" start  ");
    try:
        application_name = "";

        if None == application_name or "" == application_name:
            application_name = os.path.basename(__file__);

        print("application_name " + application_name)

        project_list = getApplicationList(application_name);
        # 排序 这里是升序
        project_list.sort();

        for item in project_list:
            print(item.getName());
            os.chdir(item.getWorkDir());

            os.system(item.getCommand());
            # 暂停几秒
            time.sleep(item.getSleep());
    except Exception as e:
         print("program error %s " %e)
    finally:
        print("finally print!")

    print(" end ");

    random_input = input(" 请输入任意字符结束. ");
