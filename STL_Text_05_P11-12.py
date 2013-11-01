# -*- coding: utf-8 -*-
# textwrap 格式化文本段落
# STL P11-12

import re

#找到所有匹配目标
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
for match in re.findall (pattern, text) : 
    print('Found "%s"' % match)

for match in re.finditer (pattern, text) : 
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))
    
def test_patterns(text, patterns = []) : 
    """ Given source text and a list of patterns, look for 
    matches for each pattern within the text and print
    them to stdout.
    """
    #Look for each pattern in the text and print the results
    for pattern, desc in patterns : 
        print('Pattern %r (%s) \n' % (pattern, desc))
        print(' %r' % text)
        for match in re.finditer(pattern, text) : 
            s = match.start()
            e = match.end()
            substr = text[s : e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print('    %s%r' % (prefix, substr))
        print
    return

if __name__ == '__main__' : 
    test_patterns('abbaaabbbbaaaaa', 
                  [('ab', "'a' followed by 'b'"), ])