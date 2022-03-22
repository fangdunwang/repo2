###函数定义：对某一个特定功能或者代码块进行封装
##定义：def 函数名称（）:
##调用：函数名称（）
# def buy_cai():
#     print('打车')
#     print('买菜')
#     print('讨价还价')
#     print('回家')
# buy_cai()
# print('哄孙子')
# buy_cai()
# print('洗马桶')
# buy_cai()
# print('打麻将')
####参数
##形参
##实参
#def 函数名称（ren,lvl）:
# #写一个四则运算的计算器
# def jisuan(a,opt,b):
#     if opt == "+":
#         print(a+b)
#     elif opt == "-":
#         print(a-b)
#     elif opt == "*":
#         print(a*b)
#     elif opt == "/":
#         print(a/b)
#     else:
#         print("滚犊子")
# jisuan(20,"+",60)
# jisuan(20,"-",60)
# jisuan(20,"*",60)
# jisuan(20,"/",60)
# jisuan(20,"%",60)

# def chi(*food):  ##*表示位置参数接受所有的动态传参 接收到为元组
#     print(food)
# chi('大米饭','烧茄子','紫菜汤')
# def chi (**food): ##**表示接受关键字的动态传参，接收为字典
#     print(food)
# chi(zhu='大米饭',fu='烧茄子')
# def func (*args,**kwargs): ##没有限制接收任何参数
#     print(args,kwargs)
# func(1234,'哈哈', a=2,)

####返回值 关于return
# a='中'
# print(ord(a)) #中字在unicode中的码位
# print(chr(20013))#给出编码位置展示文字
# for i in range(65536):
#     print(chr(i)+" ",end="")
print(help(str))