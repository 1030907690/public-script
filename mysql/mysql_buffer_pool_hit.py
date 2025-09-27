'''
ZhongZhongqing
mysql buffer pool缓存命中率
'''

import sys
import getopt
import pymysql

from decimal import Decimal, getcontext

def help():
    print('''
-h host
-p port
-u user
-pwd password
''')

def get_conn(host:str, port:int, user:str, passwd:str, db:str, charset:str):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                                charset=charset)
    return conn

def select_sql_all(cursor,sql):
    # 执行查询sql，返回所有数据
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "host=", "port="])
    # print(opts, args)

    host: str = "localhost"
    port: int = 3306
    user: str = "root"
    passwd: str = "root"
    db: str = "mysql"
    charset: str = "utf8mb4"
    conn = get_conn(host, port, user, passwd, db, charset)
    cursor = conn.cursor()


    # if opts is None or len(opts) < 1:
    #     help()

    for opt, arg in opts:
        if opt in ("-help", "--help"):
            help()
        elif opt in ("-h","--host"):
            print('script_2.py -i <input_file> -o <output_file>')
            print('or: test_arg.py --input_file=<input_file> --output_file=<output_file>')
        elif opt in ("-p", "--port"):
            input_file = arg
        else:
            help()

    global_status = dict(select_sql_all(cursor, "show global status like 'innodb%read%';"))
    print(global_status)
    # 设置精度
    getcontext().prec = 2

    print('''
 Innodb_buffer_pool_read_requests / (Innodb_buffer_pool_read_requests + Innodb_buffer_pool_read_ahead + Innodb_buffer_pool_reads)
    ''')
    res = (Decimal(global_status['Innodb_buffer_pool_read_requests']) /
                (Decimal(global_status['Innodb_buffer_pool_read_requests']) + Decimal(global_status['Innodb_buffer_pool_read_ahead']) + Decimal(global_status['Innodb_buffer_pool_reads'])))
    print(f"innodb buffer pool hit rate: {res}")







