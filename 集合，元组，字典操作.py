# -*- encoding: utf-8 -*-
'''
@File : print('i am a python file').py
@Time : 2020/02/28 09:31:40
@Author : andrewq 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#import sys
#字符串操作
str="我爱祖国\t"
str1='\"hello world\"'
str2="""the last of us
"""
if(str2.find("b",0,len(str2))==-1):
    print('no')
else:
    print("yes")
str3=str2.replace(str2,str1,-1)
print(str3)
print(len(str3))

#列表操作
score=[80,89,85,82,79,98,95,96,95,91]
for s in enumerate(score):
    print(s)
print(max(score))
print(min(score))
print(sum(score))
print(sum(score)/len(score))
#元组操作
tup1=(100,120,150,130)
print(max(tup1))
print(tup1[1:])
print(tup1[1:3])
print(tup1[-1])
print(len(tup1))
print(tup1*2)
print(tuple(list1))#列表转换成元组

#字典操作
dictstus={'alice':111,
'paul':222,
'peter':333,
'bob':444,
'jeney':555}
for k,v in dictstus.items():
    print(k,v)#遍历
print(sorted(dictstus))
print(dictstus['alice'])
dictstus['jack']=666
print(dictstus['jack'])
del dictstus['paul']
print(dictstus)
dictstus['alice']=777
print(dictstus)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
a=set('1,2,3,4,5')#集合的另外一种创建方式
print(a)
basket.add('grape')
basket.remove('banana')
basket.update([1,2,3,4])
basket.pop()
print(basket)

