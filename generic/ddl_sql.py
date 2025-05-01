import pymysql
import sys

if __name__ == '__main__':
    table_name = sys.argv[1]
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='jjjy181', charset='utf8mb4')
    cur = conn.cursor()

    # 新增
    #	cur.execute("insert into tab1(tab1_id,val) VALUES (3,3)");
    # 查询mysql版本	cur.execute("SELECT VERSION()");

    # SQL 查询语句
    sql = "show create table " + table_name
    cur.execute(sql);
    # 获取所有记录列表
    results = cur.fetchall();
    for row in results:
        # print(row,"：result");
        # print('result:', row);
        print('result:', row[1]);
    cur.close()
    conn.close()
