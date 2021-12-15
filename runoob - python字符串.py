# -*- coding: utf-8 -*-
"""
Created on Wed May 19 16:18:00 2021

@author: Administrator
"""

##转义字符

# \a响铃
print('\a')

# \000 空
print('\000')

# \n 换行
print('\n\n\n\n\n')

# \v 纵向制表符
print('hello \v world')

# \v 横向制表符
print('hello \t world')

# \f 换页
print('hello \f world')

# \r,将\r后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。
print('hello \r world')

#r或R，放在引号前，去转义化，将转义字符按照原始字符打印
print(r'\n')
print(R'\n')

##有了引号，不需要print（）函数也能打印
's'

##用%来格式化字符串
print ("我叫 %s 今年%c岁!"  %('小明', 10))

name='aa'
'hello %s' %(name)

##用str.format()的方式打印格式化字符串

#一般的例子
print('key1:{v1},key2{v2}'.format(v1='a',v2='b'))

#传入字典
jisho={'v1':'a','v2':'b'}
print('key1:{v1},key2{v2}'.format(**jisho))

#传入列表
risuto=['a','b']
print('key1:{0[0]},key2{0[1]}'.format(risuto))

##三引号,可打印各种麻烦、易误会的长字符串
'''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>'''

##f-string,格式化字符串的一种快捷的表达

namae='sugai'
f'hello,{namae}!'


f'{1+2}'


f'{jisho["v1"]},{jisho["v2"]}'
#引用字典的键名，要用双引号"

