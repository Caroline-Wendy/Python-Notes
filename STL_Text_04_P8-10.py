# -*- coding: utf-8 -*-
# textwrap 格式化文本段落
# STL P9-10

#查找字符串, 给出索引位置
import re

pattern = 'this'
text = 'Does this text match the pattern? '

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "%s"\nin "%s"\nfrom %d to %d ("%s")' % \
      (match.re.pattern, match.string, s, e, text[s:e]))

#compile()函数的用法, 转换RegexObject
regexes = [re.compile(p)
           for p in ['this', 'that']]

text = 'Does this text match the pattern? '

print('Text: %r\n' % text)

for regex in regexes:
    print('Seeking "%s" ->' % regex.pattern)
    if(regex.search(text)):
        print('match!')
    else:
        print('no match')