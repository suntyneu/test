"""
set: 类似dict，是一种key的集合，不存储value
本质：无序和无重复元素的集合

创建set
需要一个list或者tuple或者dict作为输入集合
重复元素在set中，会自动被过滤

"""
s1 = set([1, 2, 3, 4, 5, 5])
print(s1)

s2 = set((1, 2, 3, 3, 2, 1))
print(s2)

s3 = set({1: "good", 2: "nice"})
print(s3)

# 添加
# set的元素不能是字典和列表
s4 = set([1, 2, 3, 4, 5])  # 可以添加重复的，但是不会有效果
s4.add(6)
print(s4)

s5 = set([1, 2, 3, 4, 5])
s5.update([6, 7, 8])
s5.update((9, 10))
s5.update("sunty")
# 打碎插入
print(s5)

# 删除
s6 = set([1, 2, 3, 4, 5])
s6.remove(4)
print(s6)

# 遍历
print("# 遍历")
s7 = set([1, 2, 3, 4, 5])
for i in s7:
    print(i)

for index, data in enumerate(s7):
    print(index, data)
# 下标没有实在意义


# & 交集 | 并集
s8 = set([1, 2, 3])
s9 = set([2, 3, 4])
a1 = s8 & s9
print(a1)
print(type(a1))
