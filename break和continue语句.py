"""
break语句：
作用：跳出for和while循环
注意：它只能跳出距离他最近的那一层循环
    如果循环语句下面有else，break会导致下面的else不会执行。

"""
for i in range(10):
    print(i)
    if i == 5:
        break

num = 1
while num <= 10:
    print(num)
    if num == 3:
        break
    num += 1

"""
continue 语句
作用：跳过当前循环中的剩余语句，然后继续一下次循环。

"""

print("continue语句")

for i in range(10):
    if i == 3:
        continue
    print(i)
    print("*")
    print("&")
