# 需求：编写一个函数，给函数一个字符串和一个年龄，在函数内部打印出来

# 形参（形式参数）：调用函数时小括号中的变量，本质是变量
# 参数必须按顺序传递，个数目前要对应


def myprint(str, age):
    print(str, age)


# 实参（实际参数）：调用函数时给函数传递的数据，本质是值

myprint("sunck is a good man", 18)

# 编写函数，给函数两个数，返回这2个数的和


def mysum(sum1, sum2):
    sum = sum1 + sum2
    return sum
    # 执行完return语句，该函数就结束了，下面不会打印
    print("~~~~~~~~~~~~~~~~~~~~")



res = mysum(1, 2)
print(res)


# 传递参数
# 值传递：传递的是不可变类型（string，tuple, number）
def func1(num):
    num = 10


temp = 20
func1(temp)  # 将temp的值传给num ,将num的变量改为20了，不是改变temp的值，temp还是=20
print(temp)


# 引用传递：传递的可变类型(list,dict,set)
def func2(list1):
    list1[0] = 100


list2 = [1, 2, 3, 5, 6]
func2(list2)
print(list2)

# 关键字参数：允许函数调用时参数的顺序与定义时不一致


def myprint(str, age):
    print(str, age)


myprint(age=18, str="sunck is a good man")


# 默认参数
# 概念：调用函数时，如果没有传递参数，则使用默认参数。
# 使用默认参数，最后将默认参数放置最后。


def myprint(str="sunck is a good man", age=18):
    print(str, age)


myprint()


def myprint(str, age=18):  # 使用默认参数，最好将默认参数放置最后。
    print(str, age)


myprint("kaige")


# 不定长参数：能处理比定义时更多的参数
# 加了星号（*）的变量，存放所有未命名的变量参数，如果函数调用时没有
# 指定参数，它就是空元组


def func2(name, *arr):
    print(name)
    for x in arr:
        print(x)


func2("sunck", "is", "a", "afasf")


print("~~~~~~~~~~~~~~~~~~~~~~~~~~")


def func3(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(func3(1, 2, 3, 4))


# **代表键值对参数字符，和*所代表的意义类似
def func4(**kwargs):
    print(kwargs)
    print(type(kwargs))


func4(x=1, y=2, z=3)


def funcx(*args, **kwargs):  #可以传递任意参数
    pass


funcx()


# 匿名函数
# 不使用def关键字这样的语句定义函数，使用lambda来创建匿名函数
"""
特点：
1 、lambda只是一个表达式，函数体比def简单
2、lambda主体是一个表达式，不是一个代码块，仅仅只能在lambda表达式
中封装简单的逻辑
3、lambda函数有自己的命名空间，且不能访问自由参数列表之外的或全局命名空间的参数
4、虽然lambda是一个表达式且看起来只能写一行，与C C++内敛函数不同

格式：
lambda 参数1，参数2......参数n：expression
"""
sum = lambda num1, num2: num1 + num2
print(sum(1, 2))
