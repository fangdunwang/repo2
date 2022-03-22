"""
作用域：变量的访问权限
总结：里面访问外面没有问题，外面访问里面需要加return
函数可以嵌套函数
global:在局部引入全局变量
nonlocal:在局部引入外层的局部变量
"""


# a = 10
# def func():
#     global a #把外面的全局变量引入到局部
#     a = 20
# func()
# print(a)
#
# def func():
#     a = 10
#     def func2():
#         nonlocal  a #在局部引入外一层的局部变量
#         a=20
#     func2()
#     print(a)
# func()

def registration(name, age, mojor, country='CN',*args,**kwargs ):
    """
    学籍注册程序
    :param name: str
    :param age: integer
    :param mojor: str
    :param country:US ,CN,JP
    :return:
    """
    info = """
    ---------你的注册信息----------
    name:%s
    age:%s
    mojor:%s
    country:%s
    """ % (name, age, mojor, country)
    print(info)
    print(args,kwargs)


registration('张小北', 25, '计算机', 'CN')
registration('yoyo', 20, '会计')
registration('mark', 23, '计算机', 'US')
registration('山本一木',28,'物理','JP')
registration('蔡晓溪',28,'物理','CN',sex='男',phone=13525847521)
