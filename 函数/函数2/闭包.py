def func():
    a = 100

    def innner_func():
        b = 99
        print(a, b)

    print(locals())
    return innner_func


f = func()
f()
"""
闭包：
1、在外部函数中定义了内部函数
2、外部函数是有返回值得
3、返回的值是内部函数名

格式 ：
def 外部函数（）:
    def 内部函数()
    ....
    return 内部函数
"""


# 计数器
def generate_count():
    container = [0]

    def add_one():
        container[0] += 1
        print(container)

    return add_one


f = generate_count()
f()
f()
f()
f()
