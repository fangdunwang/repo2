# ##增加
# lst=['张无忌']
# #lst.append('赵本山')
# #lst.append('张三丰') ####追加
#
# lst.insert(0,'谢逊') ####插入
#
# lst.extend(['赵敏','周芷若']) ####批量添加
# print(lst)

##删除
# lst=['张无忌','张三丰','谢逊','赵敏','赵本山']
# # ret=lst.pop(4)   ####弹出删除
# # print(lst)
# # print(ret)
# lst.remove('谢逊')  ####删除元素
# print(lst)
##修改
# lst=['张无忌','张三丰','谢逊','赵敏','赵本山']
# #lst[2]='张翠山'  ####列表索引直接修改
# #print(lst)
# ##查询
# print(lst[3])   ####列表索引进行查询
##练习把所有姓张的改成王
# lst=['张无忌','张三丰','谢逊','赵敏','赵本山']
# #for item in lst:
# for i in range(len(lst)):
#     item=lst[i]
#     if item.startswith('张'):
#         new_name='王'+item[1:]
#         print(new_name)
#         lst[i]=new_name
# print(lst)

##排序
lst=[11,43,562,222,4521,11221]
lst.sort()  ####升序
lst.sort(reverse=True)  ####降序
print(lst)


