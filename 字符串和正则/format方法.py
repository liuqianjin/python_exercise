import math
temp = '编号:{:0>9s}\t公司名称：{:s}\t官网： http://www.{:s}.com'
context1 = temp.format('7','明日学院','mingri')
context2 = temp.format('8','百度','baidu')
print(context1)
print(context2)

print('1251+3950的结果是：{:.2f}元'.format(1251+3950))
print('1251+3950的结果是：{:,.2f}元'.format(1251+3950))
print('{0:.1f}用科学计数法表示为：{0:E}'.format(120000.1)) # 科学计数法
print('PI取5位小数：{:.5f}'.format(math.pi)) # 输出小数点后五位
print('{0:d}的16禁止结果是：{0:#x}'.format(100)) # 输出十六进制数
print('天才是{:.0%}的灵感，加上{:.0%}的汗水。'.format(0.01,0.99)) # 输出百分比 没有小数位
