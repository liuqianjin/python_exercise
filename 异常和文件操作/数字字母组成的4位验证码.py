# 生成4位验证码，包含数字 大小写
import random
if __name__ == '__main__':
    checkcode = ""
    for i in range(4):
        print(' ===== ',i)
        index = random.randrange(0,4) # 生成一个数 满足哪个就是哪个
        print(index)
        if index != i and index + 1 != i:
            checkcode += chr(random.randint(97,122))  # 小写
        elif index + 1 == i:
            checkcode += chr(random.randint(65,90)) # 大写
        else:
            checkcode += str(random.randint(1,9))  # 数字

    print('验证码:',checkcode)
