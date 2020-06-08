import sqlite3
# 链接数据库，数据库名字是 mrsoft.db，没有就会创建
conn = sqlite3.connect('mrsoft.db')
# 创建cursor
cursor = conn.cursor()
# 执行SQL语句，创建user表
cursor.execute('create table user (id int(10) primary key,name varchar(20))')
# 关闭游标
cursor.close()
# 关闭链接
conn.close()
