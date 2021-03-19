'''
while 语句：

while 表达式：
    语句

逻辑：当程序执行到while语句时，首先计算“表达式”的值，如果表达式的值为假，则结束整个while语句，
如果“表达式”的值为真，则执行“语句”。执行完“语句”再去计算表达式的值。

num = 0
i = 1
while i <= 100:
    num += i
    i += i
print("num =", num)

'''

sum = 0
num = 1
while num <= 100:
    sum += num
    num += 1
print("sum = %d" % sum)


num = 0
i = 1
while i <= 100:
    num += i
    i += 1
print("num =", num)

he = 0
i = 1
while i <= 1000:
    he += i
    i += 1
print(he)


str = "while 循环的基本使用 环的作用就是让指定的代码重复的执行 while 循环最常用的应用场景就是让执行的代码按照指定的次数重复执行 while 语句的基本语法"
index = 0
while index < len(str):
    print("str[%d], = %s" % (index, str[index]))
    index += 1
