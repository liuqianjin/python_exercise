# 幼儿园小朋友分苹果
# 除号用/表示，但是和C语言不同的是/得到的值总是浮点数，例如：5 / 5结果是1.0。
#python中整除用//表示是，//表示两数相除，向下取整，例如8 // 5 结果是1。

def division():
    print("\n================分苹果了===============\n")
    apple = int(input('请输入苹果的个数:'))
    children = int(input('请输入来了几个小朋友:'))
    if apple < children:
        raise ValueError("苹果太少了 不够分")
    result = apple // children
    remain = apple - result * children

    if remain > 0:
        print(apple,'个苹果，平均分给',children,'个小朋友，每人分',result,'个，剩下',remain,'个。')
    else:
        print(apple,'个苹果，平均分给',children,'个小朋友，每人分',result,'个。')

if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError:
        print("出错了，苹果不能被0个小朋友分")
    except ValueError as e:
        print("输入错误",e)
    else:
        print("分苹果顺利完成")
    finally:
        print("成功进行一次分苹果操作")
