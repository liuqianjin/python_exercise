# 匹配电话号码
import re
pattern = r'(13[4-9]\d{8})$|(15[01289]\d{8})$'
mobile = '13673498076'
match = re.match(pattern,mobile)
if match == None:
    print(mobile,'不是有效的电话')
else:
    print(mobile, '是有效的电话')

pattern1 = r'(黑客)|(抓包)|(监听)'
about= '我是一名程序员，我想研究黑客方面的书'
sub = re.sub(pattern1,';;;;;;',about)
if sub == None:
    print('安全')
else:
    print('不安全')