class Person(object):
    # 定义属性(定义变量)
    # name = ""
    # age = 0
    # height = 0
    # weight = 0

    def run(self):
        print("run")

    def eat(self, food):
        print("eat" + food)

    def __init__(self, name, age, height, weight):  # 可以有其他的参数列表
        # print(name, age, height, weight)
        self.name = name                        # self 表示要实例化对象的那个对象
        self.age = age
        self.height = height
        self.weight = weight
        print("这里是__init__")


"""
构造函数：__init__()，在使用类创建对象的时候，自动调用。
注意：如果不显示的写出构造函数，默认会自动添加一个空的构造函数。
"""

per = Person("sunck", 20, 170, 55)
per.run()
print(per.name, per.age, per.height,per.weight)

per1 = Person("lilie", 22, 175, 75)
print(per1.name, per1.age, per1.height,per.weight)
