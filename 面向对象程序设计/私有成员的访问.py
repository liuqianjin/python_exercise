class Swan:
    __neck_swan = '天鹅的脖子很长'  # 私有成员
    _neck_swan = '天鹅很好看' # 受保护的对象
    def __init__(self):
        print('__init__()  私有',Swan.__neck_swan)
        print('__init__() 受保护',Swan._neck_swan)

swan = Swan()
print('加入类名(私有):',swan._Swan__neck_swan) # 通过 成员名._类名__XXX
print('加入类名(受保护):',swan._neck_swan) # 通过 成员名._类名__XXX