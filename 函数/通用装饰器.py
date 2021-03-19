def outer(func):
    def inner(*args, **kwargs):
        # 添加修饰的功能
        print("@@@@@@@@@@@@@@@@@@")
        func(*args, **kwargs)
    return inner


@outer
def say(name, age):  # 函数的参数理论上是无限制的，但实际上不要超过6到7个
    print("my name is %s, I am %d years old" % (name, age))


say("sunty", 18)
