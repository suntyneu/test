class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("跑")

    def eat(self, food):
        print("吃" + food)

    def jump(self):
        print("跳")