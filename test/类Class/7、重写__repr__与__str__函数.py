"""
重写：将函数重写定义写一遍
__repr__(): 是给机器用的。在python解释器里面，直接敲入对象名回车后调用的方法
注意：在没有__str__()时，且有__repr__,    __str__ = __repr__

__str__(): 在调用print打印对象的时候自动调用，是给用户用的，是一个描述对象的方法。
注意： 一定要在__str__方法中添加 return ，return后门的内容就是打印对象看见的内容。
"""


class Person(object):
    def __init__(self, name, age, height, weight):  # 可以有其他的参数列表
        # print(name, age, height, weight)
        self.name = name             # self 表示要实例化对象的那个对象
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):

        return "%s-%d-%d-%d" % (self.name, self.age, self.height, self.weight)


per = Person("tom", 20, 160, 70)
# print(per.name, per.age, per.height, per.weight)
print(per)


# 优点：当一个对象的属性值很多，并且都需要打印，重写了__str__方法后，简化了代码
