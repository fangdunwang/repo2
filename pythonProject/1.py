# #转义字符
# print('hello\nworld') #n-换行
# print('hello\tworld') #t-空格
# print('hello\rworld') #r-回车
# print('hello\bworld') #b-退一格
#
# print('http:\\\\www.baidu.com') #\为转义字符 遇到网址类需要加\\
# print('老师说‘大家好’')
# #原字符 不希望字符串中的转义字符起作用 就只使用原字符 只需要在字符串之前加上r或R
# print(r'hello\nworld')
# #注意事项：使用原字符 最后一个字符不能是反斜线\

#s='hello,world'
# s1=s.upper()  ####字符串全部转大写
# # print(s1)
# s=' 你好啊，周润发  '
# s1=s.strip()   ####去掉字符串左右两边空白
# print(s1)
# s='abcdefghijklim'
# s1=s.replace('bcd','xyz')  ####将字符串替换
# print(s1)
# s='周杰伦#周润发#周星驰'
# s1=s.split('#',2)   ####将字符串进行切割
# print(s1)
# s='-'
# s1='abcd'
# s3=s.join(s1)  ####拼接一个列表中的内容
# print(s3)
# s = 'abcdefghijk'
# print(len(s))  ####求字符串长度
s='我叫周润发哈哈哈'
#s1=s.startswith('周') #####判断字符串是否以某个内容开头 也可使用in或者not in
#print(s1)
# if '发' in s:
#     print('存在')
# else:
#     print('不存在')