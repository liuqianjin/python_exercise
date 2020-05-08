str1 = '明 日 学 院 官 网  >>>  www.mingrisoft.com'
print('原字符串：',str1)
list1 = str1.split()
list2 = str1.split('>>>')
list3 = str1.split('.')
list4 = str1.split(' ',4)
print(str(list1)+'\n'+str(list2)+'\n'+str(list3)+'\n'+str(list4))
list5 = str1.split('>')
print(list5)