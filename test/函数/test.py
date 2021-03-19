"""
好好学习
天天向上

"""


def funx(fun):
    def func2():
        print("好好学习")
        fun()
    return func2


@funx
def func1():
    print("天天向上")


print(func1())




print("2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def funA(fn):
    print("C语言中文网")
    fn()  # 执行传入的fn参数
    print("http://c.biancheng.net")
    return "装饰器函数的返回值"


@funA
def funB():
    print("学习 Python")


print(funB)

print("333333333333333333333333333333333")


def fun_decorate(fun):
    def age_condition(age):
        if age < 0:
            age = 0
        fun(age)
    return age_condition


@fun_decorate
def say(age):
    print("sunck is %d years old" % age)


say(30)


