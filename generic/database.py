# -*- coding: utf-8 -*-

'''
Zhou Zhongqing
2022年5月25日14:30:11
数据库工具
'''

'''
查询表全部字段,逗号分隔
select group_concat(COLUMN_NAME) '所有字段' from information_schema.COLUMNS where table_name = '表名';
https://blog.csdn.net/qq_35427589/article/details/121767760
'''

import pymysql
import os
import json

host = ''
port = 3306
user = ''
passwd = ''
db = ''
charset = ''

# 当前用户HOME目录
file_prefix = os.path.expanduser('~')
# 配置文件全路径，文件内容如下
# {"host":"xxx.0.192","passwd":"xxxx","db":"x","user":"x","port":3306,"charset":"UTF8"}
config_path = file_prefix + '/database.json'

# ASCII码下划线的十进制数
ascii_underline_decimal_number = 95

as_str = ' as '

comma = ','


def print_sql_as(all_field_origin_array, item_cache):
    print('\n')
    print('打印as语句\n')
    length = len(all_field_origin_array)
    for index, item in enumerate(all_field_origin_array):
        as_sql_str = all_field_origin_array[index] + as_str + item_cache[index]
        # 判断是否需要加逗号
        if index < length - 1:
            as_sql_str += comma
        print(as_sql_str)

    print('----------------------------------------------\n')


def get_all_field(table_name):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                           charset=charset)
    cur = conn.cursor()
    sql = "select group_concat(COLUMN_NAME) '所有字段' from information_schema.COLUMNS where table_name = '" + table_name + "'"
    cur.execute(sql)
    # 获取所有记录列表
    results = cur.fetchall()
    all_field_origin = results[0][0]
    print(all_field_origin)
    all_field_origin_array = str(all_field_origin).split(',')
    item_cache = transfer_bean_field(all_field_origin_array)
    print(item_cache)
    print(','.join(item_cache))
    print_sql_as(all_field_origin_array, item_cache)

    # for row in results:
    #     print(row[0])
    cur.close()
    conn.close()


def search_table_by_table_name(table_name):
    '''
    搜索表根据表名模糊查询

     SELECT
        *
    FROM
        `information_schema`.`TABLES`
    WHERE
    1 =1
        -- `information_schema`.`TABLES`.`TABLE_SCHEMA` = 'xx_db' -- database
        --   and `information_schema`.`TABLES`.`CREATE_TIME` > '2021-12-20 14:36:01'  -- 从这里开始
           AND `information_schema`.`TABLES`.`TABLE_NAME` LIKE '%ark_customer%' -- 表名c_开头
           order by `information_schema`.`TABLES`.`CREATE_TIME` ;  -- 创建时间正序

    '''
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                           charset=charset)
    cur = conn.cursor()
    sql = "SELECT  * FROM `information_schema`.`TABLES` WHERE  `information_schema`.`TABLES`.`TABLE_NAME` LIKE '%" + table_name + "%' ORDER BY `information_schema`.`TABLES`.`CREATE_TIME`"
    cur.execute(sql)
    # 获取所有记录列表
    results = cur.fetchall()
    print("|         所属database    |            表名        |")
    print("| -----------------------| -----------------------|")
    for row in results:
        print("|"+format(row[1], 24) + "|" + format(row[2], 24)+"|")

    cur.close()
    conn.close()


def format(str, size):
    '''
    格式化，不足的地方补空格
    '''

    if len(str) < size:
        diff = size - len(str)
        for i in range(0, diff):
            str += ' '

    return str


def transfer_bean_field(all_field_origin_array):
    print(all_field_origin_array)
    item_cache = []
    for item in all_field_origin_array:
        if item.find('_') >= 0:
            # print(item)
            item_array = list(item)
            # print(item_array)
            item_cache_array = []
            for index, item_a in enumerate(item_array):
                # ASCII码十进制 95 是_
                if ord(item_a) == ascii_underline_decimal_number:
                    # 如果遇到_下一个字符大写，先转成ASCII码-32变大写，再转成char
                    item_array[index + 1] = chr(ord(item_array[index + 1]) - 32)
                else:
                    item_cache_array.append(item_a)
                # print(item_a)
                # print(ord(item_a))
            item_cache.append(''.join(item_cache_array))
        else:
            # 没有_直接添加
            item_cache.append(item)
    return item_cache


def read_and_set_config():
    f = open(config_path, encoding="utf-8")
    # 输出读取到的数据
    text = f.read()
    print('当前配置: ' + text)
    config_obj = json.loads(text)
    global host
    global passwd
    global db
    global user
    global port
    global charset
    host = config_obj['host']
    passwd = config_obj['passwd']
    db = config_obj['db']
    user = config_obj['user']
    port = config_obj['port']
    charset = config_obj['charset']
    # 关闭文件
    f.close()


def checking_config():
    '''
    检查配置
    '''
    if os.path.exists(config_path) is False:
        print('配置文件不存在,无法继续，请检查 ' + config_path)
        input('')


if __name__ == '__main__':
    print('start')
    checking_config()
    read_and_set_config()

    while True:
        table_name = input('请输入表名?')
        get_all_field(table_name)
        search_table_by_table_name(table_name)
    print('end')
