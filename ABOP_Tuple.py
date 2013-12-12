# -*- coding: utf-8 -*-

#====================
#File: abop.py
#Author: Wendy
#Date: 2013-12-03
#====================

#eclipse pydev, python3.3

#元组, 表示不能修改的一组的值

zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = ('monkey', 'camel', zoo) #新建元组, 不是修改
print('Number of cages in the new zoo are', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2]) #把zoo放入new_zoo的第2个位置(从0开始)
print('Last animal brought from old zoo is', new_zoo[2][2]) #元组包含元组
print('Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2])) #减去当前元素[2]和[2]的长度(3-1+3)