import sqlite3
# 链接数据库，数据库名字是 mrsoft.db，没有就会创建
conn = sqlite3.connect('mrsoft.db')
# 创建cursor
cursor = conn.cursor()
# 执行SQL语句，创建user表
cursor.execute('insert into user (id,name) values ("1","MRSOFT")')
cursor.execute('insert into user (id,name) values ("2","ANDY")')
cursor.execute('insert into user (id,name) values ("3","明日科技")')
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭链接
conn.close()
