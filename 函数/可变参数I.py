# 用* parameter 接受传入函数中的不定长参数
def printcoffee(*coffeename):
    print("\n我喜欢的咖啡是:")
    for item in coffeename:
        print(item)

printcoffee('蓝山')
printcoffee('蓝山','土耳其')

# 若是一个存在的列表作为函数的可变参数，在列表前面加上 *
parm = ['蓝山','土耳其']
printcoffee(*parm)

