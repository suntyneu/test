class Person(object):
    # 定义属性(定义变量)
    name = ""
    age = 0
    height = 0
    weight = 0

    def run(self):
        print("run")

    def eat(self, food):
        print("eat" + food)

    def open_door(self):
        print("我已经打开了冰箱门")

    def fill_ele(self):
        print("我已经把大象装进冰箱了")

    def close_door(self):
        print("我已经关上了冰箱门")


"""
实例化对象
格式：对象名 = 类名（参数列表）  没有参数列表，（）也不能省略。
"""
# 实例化一个对象
per1 = Person()
print(per1)

per2 = Person()
print(per2)

per2.close_door()
