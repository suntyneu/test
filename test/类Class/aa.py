class Test1(object):
    # name = "sunck"

    def study(self):
        print("sunck good stydy")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("这里是__init__")


ok = Test1("sunty", 19)
print(ok.name, ok.age)


class Person(object):
    def run(self):
        print("run")

    def __init__(self, name, age, height, weight):  # 可以有其他的参数列表
        # print(name, age, height, weight)
        self.name = name  # self 表示要实例化对象的那个对象
        self.age = age
        self.height = height
        self.weight = weight
        print("这里是__init__")


per = Person("sunck", 20, 170, 55)
print(per.name, per.age, per.height, per.weight)
