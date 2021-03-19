"""
找最大值：
在列表中找最大值，自己封装一个函数
"""

list1 = [234, 124564, 3, 11, 5555, 22]


def max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    print("max=", max)


max(list1)

s = {1, 3, 5, 7, 9}
list2 = []
index = 0
for i in s:
    t1 = (index, i)
    list2.append(t1)
    index += 1
print(list2)
print("~~~~~~~~~~~~")

for index, v in list2:
    print(index, v)
