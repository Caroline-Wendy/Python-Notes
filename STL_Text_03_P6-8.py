# -*- coding: utf-8 -*-
# textwrap 格式化文本段落
# STL P6

sample_text = '''
    The textwrap module can be used to format text for output in 
    situations where pretty-printing is desired. It offers 
    programmatic functionality similar to the paragraph wrapping 
    or filling features found in many text editors.
    '''
#填充段落
#fill()生成格式化文本
import textwrap

print('No dedent:\n')
print(textwrap.fill(sample_text, width=50))

#dedent()去除缩进
dedented_text = textwrap.dedent(sample_text);
print('Dedented: ')
print(dedented_text)

#结合dedent和fill
#strip()用于去除字符串的首尾字符
dedented_text = textwrap.dedent(sample_text).strip()
for width in [45, 70]:
    print('%d Columns: \n'  % width)
    print(textwrap.fill(dedented_text, width=width))
    print()
    
#单独控制第一行的缩进
dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text,
                    initial_indent = '',
                    subsequent_indent=' '*4,
                    width=50,
                    ))