# -*- coding: utf-8 -*-

'''
启动应用 2019年12月13日20:16:13  sqlite版本
'''

import os
import time
import sqlite3


# 执行的应用程序
class ApplicationRunTime:
    def __init__(self, id, name, workDir, status, sort, sleep, command, remarks, date):
        self.id = id;
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
        # 时间
        self.date = date;

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



def execCmd(command):
    r = os.popen(command)
    text = r.read()
    r.close()
    print(text)
    return text


def getApplicationList(application_name):
    conn = sqlite3.connect('sqlite.db')
    sql = "SELECT id,name,work_dir ,status, sort,sleep,command,remarks,date FROM  application where 1=1 and status='1' and application_name = '" + application_name + "'  order by  sort asc";
    cursor = conn.execute(sql);

    project_list = [];
    for row in cursor:
        application = ApplicationRunTime(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]);
        project_list.append(application);
    conn.close();
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

            execCmd(item.getCommand())
            #os.system(item.getCommand());
            # 暂停几秒
            time.sleep(item.getSleep());
    except Exception as e:
         print("program error %s " %e)
    finally:
        print("finally print!")

    print(" end ");
    random_input = input(" 请输入任意字符结束. ");
