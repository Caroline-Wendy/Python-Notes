# -*- coding: utf-8 -*-

#====================
#File: abop.py
#Author: Wendy
#Date: 2013-12-03
#====================

#eclipse pydev, python3.3

shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase') #求列表的长度
print('These items are:', end=' ') #end表示不是换行, 最后结束的是' '
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist) #打印列表[]

print('I will sort my list now')
shoplist.sort() #首字母排序
print('Sorted shopping list is', shoplist)
print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0] #删除首元素
print('I bought the', olditem)
print('My shopping list is now', shoplist) #打印剩下的列表