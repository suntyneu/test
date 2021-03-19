# def decorate(fun1):
#     def inner():
#         txt2 = "装饰过的"
#     return inner
#     func1()
#
# #
#
#
# @decorate
# def func(txt):
#     txt = "大门"
#     print(txt)
#
#
# func(fun)


def decorate(fun):
    def inner():
        print("~~~~~~~~~~~~~~")
        fun()
    return inner


@decorate
def func1():
    print("aaa")


func1()
"""
1、func1作为被装饰的函数。
2、将被装饰函数作为参数传给装饰器decorate.
3、执行decorate函数
4、将返回值传给func1
"""
