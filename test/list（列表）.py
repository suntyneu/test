"""
存储5个人的，求他们平均年龄
使用列表，存储更多的数据。
列表本质是一种有序的集合。

格式：列表名 = [列表选项1，列表选项2....]
"""
list1 = []
print(list1)

# 创建带有元素的列表
list2 = [18, 20, 22, 19, 21]
print(list2)

# 注意：列表中元素的数据可以是不同类型
list3 = [1, 2, 3, "asdfadsf", True]
print(list3)

# 列表元素的访问 注意不要越界
# 取值 格式：列表名[下标]
list4 = [1, 2, 3, "asdfadsf", True]
print(list4[2])

# 替换
list4[2] = 300
print(list4)

# 列表组合
list5 = [3, 3, 5]
list6 = list5 + list4
print(list6)

# 列表的重复
list7 = [1, 2, 3]
print(list7 * 3)

# 判断元素是否在列表中

list8 = [1, 2, 3, 4, 6, 9, 10]
print(3 in list8)
print(5 in list8)

# 列表截取
list9 = [1, 2, 3, 4, 6, 9, 10]
print(list9[2:5])

# 二维列表
list10 = [[1, 3], [2, 3, 6], ["qrf", "eqwrew", "qreqwer"]]
print(list10)

# 列表方法
# append 在列表末尾添加新的元素
list12 = [1, 2, 3, 4, 5, 4, [3, 5, 7]]
list1.append([3, 5, 7])
print(list12)
print(list12)

# extend 在末尾一次性追加另一个列表中的多个值
list13 = [1, 2, 3, 4, 5]
list13.extend([6, 7, 8])
print("list13=", list13)

# insert 在下标出添加一个元素，原来的元素向后移动
list14 = [1, 2, 3, 4, 5]
list14.insert(2, [100, 220])
print("list14=", list14)

# pop 删除列表下标的元素，默认是最后一个元素list[-1],并返回删除的数据
list15 = [1, 2, 3, 4, 5]
list15.pop()
print(list15)
list15.pop(2)
print(list15)
print(list15.pop(2))
print(list15)


# remove 移除列表中某个元素，第一个匹配的。
list16 = [1, 2, 3, 4, 5, 6, 7, 8]
list16.remove(4)
print(list16)

# clear 清除列表中所有的数据
list17 = [1, 2, 3, 4, 5, 6, 7, 8]
list17.clear()
print(list17)

print("@222222222222")
# index 从列表中查找某个值的第一个匹配索引
list18 = [1, 2, 3, 4, 5, 6, 3, 3, 5, 5, 3, 6, 7, 8, 3]
index18 = list18.index(5)
index19 = list18.index(3, 4, 9)
print(index18, index19)

# 列表中元素个数 len
list20 = [1, 2, 3, 4, 6, 3, 3, 11]
print("list20元素个数是：", len(list20))

# 列表中最大值 max；列表中最小值min；
list21 = [1, 2, 3, 4, 6, 3, 3, 11]
print(max(list21))

# count 查看元素在列表中出现的次数
list23 = [1, 2, 1, 3, 1, 1, 1, 3, 11, 3, 1]
print(list23.count(1), list23)
num = 0
strt = list23.count(1)
while num < strt:
    list23.remove(1)
    num += 1
print(list23)

# 倒叙 reverse
list25 = [1, 2, 4, 6, 3, 11]
list25.reverse()
print(list25)

# 排序 sort 升序
list26 = [2, 11, 3, 1, 5, 8, 9, 4]
list26.sort()
print(list26)

# 拷贝
# 浅拷贝 引用拷贝
list27 = [1, 2, 3, 5, 6]
list28 = list27
list28[1] = 200
print(list27, list28)
print(id(list27), id(list28))

# 深拷贝 内存的拷贝
list29 = [1, 2, 3, 4, 5]
list30 = list29.copy()
list30[1] = 200
print(list29, list30)

# 将元组转换成列表
list31 = list((1, 2, 3, 4))
print(list31)

"""
numerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

Python 2.3. 以上版本可用，2.6 添加 start 参数。

语法
以下是 enumerate() 方法的语法:

enumerate(sequence, [start=0])
参数
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。
返回值
返回 enumerate(枚举) 对象。

实例
以下展示了使用 enumerate() 方法的实例：

>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))       # 下标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
普通的 for 循环
>>>i = 0
>>> seq = ['one', 'two', 'three']
>>> for element in seq:
...     print i, seq[i]
...     i +=1
...
0 one
1 two
2 three
for 循环使用 enumerate
>>>seq = ['one', 'two', 'three']
>>> for i, element in enumerate(seq):
...     print i, element
...
0 one
1 two
2 three
"""

