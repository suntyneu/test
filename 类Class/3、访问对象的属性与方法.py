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
        print("我已经不安比冰箱门")

"""
实例化对象
格式：对象名 = 类名（参数列表）  没有参数列表，（）也不能省略。
"""
per = Person()


"""
访问属性
格式：对象名.属性名
赋值：对象名.属性名 = 新值
"""
# 访问属性
per.name = "tom"
per.age = 18
per.height = 160
per.weight = 90
print(per.name, per.age, per.height, per.weight)

"""
访问方法
格式：对象名.方法名(参数列表)
"""

# 访问方法
per.open_door()
per.fill_ele()
per.close_door()
per.eat("apple")

