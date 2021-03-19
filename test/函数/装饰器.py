"""
装饰器
概念：一个闭包，把一个函数当成参数，返回一个替代版的函数。
本质上就是一个返回函数的函数
"""


def func1():
    print("sunck is a good man")


def outer(func):
    def inner():
        print("*******************")
        func()
    return inner


# f 是函数func1的加强版本
f = outer(func1)
f()

"""
那么，函数装饰器的工作原理是怎样的呢？假设用 funA() 函数装饰器去装饰 funB() 函数，如下所示：
纯文本复制
#funA 作为装饰器函数
def funA(fn):
    #...
    fn() # 执行传入的fn参数
    #...
    return '...'
@funA
def funB():
    #...

实际上，上面程序完全等价于下面的程序：
def funA(fn):
    #...
    fn() # 执行传入的fn参数
    #...
    return '...'
def funB():
    #...
funB = funA(funB)
通过比对以上 2 段程序不难发现，使用函数装饰器 A() 去装饰另一个函数 B()，其底层执行了如下 2 步操作：
将 B 作为参数传给 A() 函数；
将 A() 函数执行完成的返回值反馈回  B。

"""

#  funA 作为装饰器函数


def funA(fn):
    print("C语言中文网")
    fn()  # 执行传入的fn参数
    print("http://c.biancheng.net")
    return "装饰器函数的返回值"


@funA
def funB():
    print("学习 Python")


print(funB)

"""
显然，被“＠函数”修饰的函数不再是原来的函数，而是被替换成一个新的东西（取决于装饰器的返回值），
即如果装饰器函数的返回值为普通变量，那么被修饰的函数名就变成了变量名；
同样，如果装饰器返回的是一个函数的名称，那么被修饰的函数名依然表示一个函数。

实际上，所谓函数装饰器，就是通过装饰器函数，在不修改原函数的前提下，来对函数的功能进行合理的扩充。
"""

"""
带参数的函数装饰器
在分析 funA() 函数装饰器和 funB() 函数的关系时，细心的读者可能会发现一个问题，
即当 funB() 函数无参数时，可以直接将 funB 作为 funA() 的参数传入。
但是，如果被修饰的函数本身带有参数，那应该如何传值呢？

比较简单的解决方法就是在函数装饰器中嵌套一个函数，该函数带有的参数个数和被装饰器修饰的函数相同。例如：
"""

print("last")


def funA(fn):
    # 定义一个嵌套函数
    def say(arc):
        print("Python教程:", arc)
        say(arc)
    return fn


@funA

def funB(arc):
    print("funB():", arc)


funB("http://c.biancheng.net/python")
