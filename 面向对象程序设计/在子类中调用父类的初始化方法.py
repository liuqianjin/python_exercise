class Fruit:
    def __init__(self,color = "绿色"):
        Fruit.color = color
    def harvest(self,color):
        print('水果四：'+ self.color + '的！')
        print('水果已经收获。。。')
        print('水果原来是:'+Fruit.color + '的')


class Apple(Fruit):
    color = '红色'
    def __init__(self):
        print("我是苹果")
        super().__init__()

class Sapodille(Fruit):
    def __init__(self,color):
        print('\n我是人参果')
        super().__init__(color) # 更新默认颜色

    def harvest(self,color):
        print('人参果：'+color+'的！')
        print('人参果已经收获。。。')
        print('人参果原来是:'+Fruit.color + '的')

apple = Apple()
apple.harvest(apple.color) # 子类的__init__()方法中的默认值
sapodilla = Sapodille('白色')  # 子类初始化指定
sapodilla.harvest('金黄色带紫色条纹')