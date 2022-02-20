# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

tuple = ('abcd', 786, 2.23, 'nowcoder', 70.2)
tinytuple = (123, 'nowcoder')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组
print('-------------------------')
# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
tuple3 = (11, 1, 3, ["sdad", "sdaqwe", 123, True])
print(tuple3)
tuple3[3][3] = False
print(tuple3)
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tuple1 = ()  # 构造一个空元组
tuple2 = (10,)  # 构造一个只含1个元素的元组，必须加 ,号
# string、list 和 tuple 都属于 sequence（序列）。

