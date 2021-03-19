# 装饰器带参数  就必须也有三层函数，第三层函数给第二层，第二层函数给第一层
"""
装饰器带参数  三层函数，第三层函数给第二层，第二层函数给第一层
最外层负责接收装饰器的参数
中间层负责接收函数
内层负责接收函数的参数
"""


def outer(a):  # 第一层：负责接收装饰器的参数
    def decorate(func):  # 第二层：负责接收函数
        def inner(*args, **kwargs):  # 第三层：负责接收函数的参数
            func(*args)
            print("-------------》铺地板{}快".format(a))
        return inner
    return decorate


@outer(50)
def house(time1):
    print("我是在{}这个日期拿到的房子，是毛坯房".format(time1))


house("2019-12-5")


@outer(2000)
def street():
    print("修路")


street()
