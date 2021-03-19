"""
字典
概述：使用键-值（key-value)存储，具有极快的查找速度

key的特性：
1、字典中的key必须唯一
2、key必须是不可变队形
3、字符串、整数等都是不可变的，可以作为Key
4、list是可变的，不能作为key

注意：字典是无须的
学生姓名为key，成绩为值
"""
dict1 = {"tom": 60, "lilei": 70}

# 元素的访问
# 获取:字典名[key]
print(dict1["lilei"])
print(dict1["tom"])
# print(dict1["sunck"])  # 没有会报错
print(dict1.get("sunck"))  # 用get不会报错

# 添加
dict1["hanmeimei"] = 99
dict1["lilei"] = 90
# 因为一个key对应一个value，所以斗刺对一个key的value赋值，其实就是修改值


# 删除
dict1.pop("tom")
print(dict1)

# 遍历
for key in dict1:
    print(key, dict1[key])

print(dict1.values())  # 打印出一个列表，values所有的值
for value in dict1.values():  # [80, 99]
    print(value)

print(dict1.items())  # dict_items([('lilei', 90), ('hanmeimei', 99)])
for k, v in dict1.items():
    print(k, v)


for i, v2 in enumerate(dict1):
    print(i, v2)


# 和list比较
# 1、查找和插入的速度极快，不会随着key-value的增加而变慢
# 2、需要占用大量的内场，内存浪费多

str1 = "sunty is a good man! sunty is a good man! sunty is a good man! sunty is a good man! sunty is a good man! "
list1 = str1.split()
d = {}
print(list1)
for v in list1:
    c = d.get(v)
    if c == None:
        d[v] = 1
    else:
        d[v] += 1
print(d)
"""
1、已空格切割字符串
2、循环处理列表中的每个元素
3、以元素当做key去一个字典中提取数据
4、如果没有提取到，就以该元素作为key的values修改,值加1
5、如果提取到，将对应的key的value值修改，值加1
6、根据输入的字符串中当做key再去字典取值
"""

