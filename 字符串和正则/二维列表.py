str1 = '千山鸟飞绝'
str2 = '万径人踪灭'
str3 = '孤舟蓑笠翁'
str4 = '独钓寒江雪'

verse = [list(str1),list(str2),list(str3),list(str4)] #将str转为list，成为二维数组
print("\n-- 横版 --\n")
for i in range(len(verse)):
    for j in range(len(verse[0])):
        if j == 4:
            print(verse[i][j])
        else:
            print(verse[i][j],end='')

verse.reverse()
print("\n-- 竖版 --\n")
for i in range(5):
    for j in range(4):
        if j == 3:
            print(verse[j][i])
        else:
            print(verse[j][i],end='')
