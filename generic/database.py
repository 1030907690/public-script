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

host = '172.19.0.192'

port = 2881
user = 'root'
passwd = 'root@gs123'
db = 'scrm'
charset = 'UTF8'


def get_all_field(table_name):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                           charset=charset);
    cur = conn.cursor();
    sql = "select group_concat(COLUMN_NAME) '所有字段' from information_schema.COLUMNS where table_name = '" + table_name + "'"
    cur.execute(sql);
    # 获取所有记录列表
    results = cur.fetchall()
    all_field_origin = results[0][0]
    print(all_field_origin)
    all_field_origin_array = str(all_field_origin).split(',')
    item_cache = transfer_bean_field(all_field_origin_array)
    print(item_cache)
    print(','.join(item_cache))

    # for row in results:
    #     print(row[0])
    cur.close()
    conn.close()


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
                if ord(item_a) == 95:
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

if __name__ == '__main__':
    print('start')
    table_name = input('请输入表名?')
    get_all_field(table_name)
    print('end')
