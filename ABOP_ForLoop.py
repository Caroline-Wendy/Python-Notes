# -*- coding: utf-8 -*-

#====================
#File: abop.py
#Author: Wendy
#Date: 2013-12-03
#====================

#eclipse pydev, python3.3

name = 'Wendy'
friend = 'Caroline'
running = True #true首字母大写
times = range(1, 4)

print('Who is the author? ( you have 3 times)')

for i in times : #表示[1,4), 3个数, 1, 2, 3, for是顺次指向下一个元素, 无法更改i的值
    guess = str(input("Enter an name(time: {0}) : ".format(i)))
    
    if guess == name : 
        print('Congratulation, you guessed it! ')
        break #循环终止
    elif guess == friend : #额外的机会, 不能修改i的值, 改变判断次序
        print('Oh, you know my friend! Give you one extra times! ')
        guess = str(input("Enter an name(time: {0}) : ".format(i)))
        if guess == name : 
            print('Congratulation, you guessed it! ')
            break #循环终止'''
    elif guess[0] != 'W': #elif的写法
        print("Sorry, my first letter is 'W'. ")
    else :
        print("Please, continue to guess. ")
else : #while语句的else
    print('Sorry, you have no times.')
    
print('done')
