# -*- coding: utf-8 -*-
# 高级模板
import string
import re

template_text = '''
Delimiter: %%
Replaced: %with_underscore
Ignored: %notunderscored
'''

d = {'with_underscore':'replaced', 'notunderscored':'not replaced',}
class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'
    
t = MyTemplate(template_text)
print('Modified ID pattern: ')
print(t.safe_substitute(d))

#覆盖Python属性
t = string.Template('$var')
print(t.pattern.pattern)

#新的模板
class MyTemplate(string.Template) :
    delimiter = '{{'
    pattern = r'''
    \{\{(?:
    (?P<escaped>\{\{) |
    (?P<named>[_a-z][_a-z0-9]*)\}\} |
    (?P<braced>[_a-z][_a-z0-9]*)\}\} | 
    (?P<invalid>) 
    )
    '''
t= MyTemplate('''
{{{{
{{var}}
''')

print('MATCHES:', t.pattern.findall(t.template))
print('SUBSTITUTED', t.safe_substitute(var='replacement'))