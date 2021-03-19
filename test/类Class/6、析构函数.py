"""
析构函数：__del__():  释放对象时候自动调用
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

    def __del__(self):
        print("这里是析构函数")


per = Person("tom", 20, 160, 70)
# 释放对象
# del per     # 对象释放以后不能再访问
# print(per.age)


# 在函数里定义的对象，会在函数结束时自动释放，用来减少内存空间的浪费
def func():
    per2 = Person("aa", 1, 1, 1)


func()
