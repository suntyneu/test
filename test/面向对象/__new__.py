# __new__
"""
触发时机：初始化对象时出发（不是实例化对象，但是和实例化在一个操作中）
"""


class Person(object):
    def __init__(self, name):
        print("---------->init")
        self.name = name

    def __new__(cls, *args, **kwargs):
        print("------------>new")


p = Person("jack")


class newStyleClass(object):
    # In Python2, we need to specify the object as the base.
    # In Python3 it's default.

    def __new__(cls):
        print("__new__ is called")
        return super(newStyleClass, cls).__new__(cls)

    def __init__(self):
        print("__init__ is called")
        print("self is: ", self)


newStyleClass()
