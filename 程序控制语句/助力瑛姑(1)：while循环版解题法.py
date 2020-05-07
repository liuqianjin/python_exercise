'''
瑛姑问题：今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何?
解：用while循环从1开始依次尝试，直到满足条件则退出。
    首先定义一个计数的number和一个作为循环条件的变量的none,编写while
    将变量number+1，且判断number是否符合条件，符合条件将none设置为假，退出循环。
'''

number = 1
print('有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何?\n')
none = True
while none:
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
        print("答曰：这个数是",number)
        none = False
    else:
        number += 1

