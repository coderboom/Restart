"""
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""
parame = {value01,value02,...}
或者
set(value)
"""
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)
student.pop()
print(student)

if 'Rose' in student:
    print('Rose in student')
else:
    print('Rose in`t in student')

# set可以进行集合运算
a = set('asbiybraohdahdashsdhabuas')
b = set('dnasoyasndosiudweqhoahd')

print(a)
print(a - b)  # a 和 b的差集,返回的是a中有，b中没有的
print(a | b)  # a和b的并集 ，
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素
