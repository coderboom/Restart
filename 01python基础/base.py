# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
#
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型
# 给变量的赋值是什么类型，就可以把变量理解成什么类型的变量
a, b, c, d = 1, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))  # type()不会认为子类是一种父类类型。
print(isinstance(111, int))  # isinstance()会认为子类是一种父类类型。


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)
# !/usr/bin/python3
print('--------------------------')
str = 'Nowocder'  # Python 没有单独的字符类型，一个字符就是长度为1的字符串

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str * 2)
print(str + "TEST")  # 连接字符串

print('Now\ncoder')
print(r'Now\ncoder')  # r ———— 原生的 ， 防止转义字符。
