# List（列表）
# List（列表） 是 Python 中使用最频繁的数据类型。
#
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
#
# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
#
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

list = ['abcd', 786, 2.23, 'nowcoder', 70.2]
tinylist = [123, 'nowcoder']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表


# 将字符串翻转
def reverseWords(input):
    # ——在指定的分隔符处拆分字符串，返回一个列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' _-_ '.join(inputWords)

    return output


if __name__ == "__main__":
    input = 'I like nowcoder'
    rw = reverseWords(input)
    print(rw)
