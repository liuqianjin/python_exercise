# 练习体会值传递和参数传递的区别
def demo(obj):
    print("原值：",obj)
    obj += obj

print("-----值传递————————")
mot = '唯有在追赶的时候，你才能真正的奔跑'
print("函数调用前：",mot)
demo(mot)
print("函数调用后：",mot)

print("-----参数传递————————")
mot = ['张三',"李四"]
print("函数调用前：",mot)
demo(mot)
print("函数调用后：",mot)
