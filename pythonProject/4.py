####文件操作
"""
open(文件路径，mode="",encoding="")
open('文件名'，mode='r',encoding='')
"""


#f = open("国产自拍.txt", mode='r', encoding='utf-8')
# content = f.read()
# print(content)
# line=f.readline() #只读一行
# print(line)
# content=f.readlines() #一次性读出来形成列表
# print(content)
# for line in f:  #最重要的读取方式
#     print(line.strip())

# ###写入
# f=open('一起屠龙记.txt',mode='w',encoding='utf-8')
# f.write('张三丰')
# f.close()
# lst= ['张无忌','赵敏','谢逊','周芷若']
# f=open('一起屠龙记.txt',mode='w',encoding='utf-8')
# for item in lst:   #写入列表中的内容 最重要的一种写入方法
#     f.write(item)
#     f.write('\n')
#     f.close()
##append  此模式是追加内容不改变原内容
# f=open('一起屠龙记.txt',mode='a',encoding='utf-8')
# f.write('白眉鹰王')
# f.close()

##with  自动关闭文件 不需加close
with open('一起屠龙记.txt',mode='r',encoding='utf-8') as f:
    for line in f:
        print(line.strip())
##读写非文本文件需要加b
with open('   .jpeg',mode='rb') as f:
    for line in f:
        print(line.strip())



