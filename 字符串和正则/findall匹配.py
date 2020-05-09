import re
pattern = r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
str1 = '127.0.0.1 192.168.1.66'
match = re.findall(pattern,str1)
print(match)
print()
for item in match:
    print(item[0])