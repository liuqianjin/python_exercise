import sqlite3
# 链接数据库，数据库名字是 mrsoft.db，没有就会创建
conn = sqlite3.connect('mrsoft.db')
# 创建cursor
cursor = conn.cursor()
# 执行SQL语句，创建user表

cursor.execute('delete from user where id = ?',(1,)) #删除ID是1 的数据
# 将1的名字修改为MR

cursor.execute('select * from user')

result = cursor.fetchall() # fetchone.fetchmany.fetchall..打印一个，很多个（数字），全部
print(result)

# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭链接
conn.close()
