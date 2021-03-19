"""
self: 代表类的实例，而非类

哪个对象调用方法，那么该方法中的self就代表那个对象

self.__class__ 代表类名
"""


class Person(object):
    def run(self):
        print("run")

    def eat(self, food):
        print("eat" + food)

    def say(self):
        print("Hello!my name is %s,I am %d years old" % (self.name, self.age))

    def __init__(self, name, age, height, weight):  # 可以有其他的参数列表
        # print(name, age, height, weight)
        self.name = name             # self 表示要实例化对象的那个对象
        self.age = age
        self.height = height
        self.weight = weight


per1 = Person("tom", 20, 160, 70)
per1.say()
per2 = Person("sunck", 22, 180, 78)
per2.say()
