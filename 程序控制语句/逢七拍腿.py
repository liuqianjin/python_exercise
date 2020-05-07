'''
游戏规则：
从1开始数数，尾数是7或者是7的倍数，则不报数，拍腿，计算1-99里面拍了几次腿
'''
count = 0
for i in range(1,100):
    if i % 10 == 7 or i % 7 == 0:
        count += 1
        continue
print('一共拍腿'+str(count)+'次。')