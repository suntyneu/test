"""
for 语句
格式：
for 变量名 in 集合：
    语句

逻辑：按顺序取 "集合" 中的每个元素，赋值给 "变量"
    在执行语句。如此循环往复，直到取完“集合”中的元素截止。

range([start,]end[,step]) 函数 列表生成器  start 默认为0 step 步长默认为1
功能：生成数列
for i in [1, 2, 3, 4, 5]:
    print(i)
"""

a = range(12)
print(a)
for x in range(12):
    print(x)
for y in range(2, 20, 2):
    print(y)

# enumerate 同时指定下标和元素
for index, m in enumerate([1, 2, 3, 4, 5]):  # index， m = 下标，元素
    print(index, m)

# for 实现1+2+3+...100的和

sum = 0
for n in range(1, 101):
    sum += n
print(sum)
