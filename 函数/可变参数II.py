# 如果多个数据以字典形式传入函数参数。用**parameter
def printsign(**sign):
    print()
    for key , value in sign.items():
        print("["+key+"]的星座是:"+value)

printsign(绮梦='水瓶座', 冷意义='金牛座')


# 若是已经存在的字典
dict1 = {'绮梦':'水瓶座','冷意义':'金牛座'}
printsign(**dict1)