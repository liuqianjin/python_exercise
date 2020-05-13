# 满500打9折，满1000打8折，满2000打7折，满3000打6折,计算实付金额
def fun_checkout(money):
    # money 是保存钱的列表。返回商品的合计金额和折扣后的金额
    money_old = sum(money)
    money_new = money_old
    if 500 <= money_old < 1000:
        money_new = '{:.2f}'.format(money_old*0.9)
    if 1000 <= money_old < 2000:
        money_new = '{:.2f}'.format(money_old*0.8)
    if 2000 <= money_old < 3000:
        money_new = '{:.2f}'.format(money_old*0.7)
    if 3000 <= money_old :
        money_new = '{:.2f}'.format(money_old*0.6)
    return money_old,money_new

print("\n ==== 开始结算 =====")
list_money = []  # 定义保存商品金额的列表
while True:
    inmoney = float(input("输入商品金额:（输入0表示结束）"))
    if int(inmoney) == 0:
        break
    else:
        list_money.append(inmoney)

money = fun_checkout(list_money)
print("合计金额:",money[0],'应付金额：',money[1])
