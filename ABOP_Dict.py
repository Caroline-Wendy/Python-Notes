# -*- coding: utf-8 -*-

#====================
#File: abop.py
#Author: Wendy
#Date: 2013-12-03
#====================

#eclipse pydev, python3.3

#字典, 即map, dict

an = { 'Caroline' : 'A beautiful girl.',
            'Wendy' : 'A talent girl.',
            'Spike' : 'A good boy' 
            }

print (an)
print ("Who is Caroline?", an['Caroline'])
del an['Spike']
print('There are {0} girls.'.format(len(an)))

for name, property in an.items() : #遍历字典的项
    print('{0} is that {1}'.format(name, property))
    
an['Ruby'] = 'A pretty girl'

if 'Ruby' in an : #判断元素是否存在
    print("The new one Ruby is that", an['Ruby'])