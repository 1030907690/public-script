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

if __name__ == '__main__':
    print('start')
