import sqlite3
# 链接数据库，数据库名字是 mrsoft.db，没有就会创建

conn = sqlite3.connect('mrsoft1.db')

def menu(): # 菜单，显示主界面
    print("-" * 30)
    print("""
     学生管理系统
    1.添加学生信息
    2.删除学生信息
    3.修改学生信息
    4.查询学生信息
    5.显示所有信息
    6.退出系统
        """)
    print("-" * 30)

def create_info():
    # 创建cursor
    cursor = conn.cursor()
    # 执行SQL语句，创建user表
    cursor.execute('create table if not exists user (id int(10) primary key,name varchar(20))')
    # 关闭游标
    cursor.close()
    # 关闭链接
    conn.close()

def insert_info(): # 增加
    # 创建cursor
    cursor = conn.cursor()
    while True:
        user_id = input("please input the id:")
        username = input('please input the name:')

        insert_sql = 'insert into user (id,name) values (:st_id,:st_name)'
        cursor.execute(insert_sql,{'st_id': user_id,'st_name': username})
        # 提交事务
        conn.commit()
        print('提交成功')

        input_over = input('input over ?:')
        if input_over == 'y' or input_over == 'Y' or input_over == 'yes':
            break
        elif input_over == 'n' or input_over == 'N' or input_over == 'no':
            print("取消取出")
        else:
            print("输入错误，退出失败")
    #
    # # 关闭游标
    cursor.close()

def show_info(): # 显示
    cursor = conn.cursor()
    # 执行SQL语句，创建user表
    cursor.execute('select * from user')

    result = cursor.fetchall()  # fetchone.fetchmany.fetchall..打印一个，很多个（数字），全部
    print(result)

    # 提交事务
    conn.commit()

def del_info(): # 删除
    cursor = conn.cursor()
    show_info()
    id = input('请输入要删除的课程的id:')
    sql = 'delete from user where id = (:id)'
    cursor.execute(sql, {'id': id})
    conn.commit()
    print('删除成功，现有的课程为：')
    show_info()

def upgrade_info(): # 修改
    cursor = conn.cursor()

    print('现有的学生为：')
    show_info()

    id = input('请输入要修改的学生的id：')
    new_name = input('请输入新的学生名字：')
    sql = 'update user set name = (:name) where id = (:id) '
    cursor.execute(sql, {'name': new_name,  'id': id})
    conn.commit()
    print('修改成功，现有的课程为：')
    show_info()

def query_info(): # 查询
    cursor = conn.cursor()
    id = input('请输入需要查询的学生id:')
    sql = 'select * from user where id = (:id)'
    result = cursor.execute(sql,{'id':id})
    conn.commit()
    print('学生id\t学生姓名')
    for i in result:
        print('\t' + str(i[0]) + '\t' + i[1])



def main(): # 菜单主函数
    create_info()
    while True:
        menu()
        number = input("请输入想要的功能：")
        if number == str(1):
            insert_info()
        elif number == str(2):
            del_info()
        elif number == str(3):
           upgrade_info()
        elif number == str(4):
            query_info()
        elif number == str(5):
            show_info()
        elif number == str(6):
            whether_to_quit = input("是否退出(y/n)")
            while True:
                if whether_to_quit == 'y' or whether_to_quit == 'Y' or whether_to_quit == 'yes':
                    print("已退出")
                    exit()
                elif whether_to_quit == 'n' or whether_to_quit == 'N' or whether_to_quit == 'no':
                    print("取消取出")
                    break
                else:
                    print("输入错误，退出失败")
                    break
        else:
            print("输入错误，请重新输入")

if __name__ == '__main__':
    main()
