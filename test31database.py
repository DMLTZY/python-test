import pymysql

conn = pymysql.connect(user='root', password='zhangyue', host='127.0.0.1', db='pytest20160818')
cur = conn.cursor()

# cur.execute('create table tb1(id INT, name VARCHAR(10))')
cur.execute('select * from tb1')
print(cur.fetchall())
print(cur.description)

cur.close()
conn.close()