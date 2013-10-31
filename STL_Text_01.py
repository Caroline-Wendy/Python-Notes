# -*- coding: utf-8 -*-
#from Python STL

#首字母大写
import string
s = 'Hello, I like a girl. She is very pretty! '
print (s)
print (string.capwords(s))

#修改文件的字符 Python3.3不支持
leet = s.maketrans('abcde', '12345')
print (s.translate(leet))

#模板
values = {'var': 'foo'}
t = string.Template("""
Variable: $var
Escape: $$
Variable in text: ${var}iable
""")
print('TEMPLATE: ', t.substitute(values))
s = """
Variable: %(var)s
Escape: %%
Variable in text: %(var)siable
"""
print('INTERPOLATION: ', s%values)

#安全的模板方法, 避免模板不全产生异常
values = {'var' : 'foo'}
t = string.Template("$var is here but $missing is not provided")
try:
    print('substitute() :', t.substitute(values))
except KeyError as err:
    print('Error: ', str(err))
print('safe_substitute() :', t.safe_substitute(values))    