class Person(object):
    def run(self):
        print(self.__money)
        print("run")

    def __init__(self, name, age, height, weight, money):  # 可以有其他的参数列表
        # print(name, age, height, weight)
        self.name = name             # self 表示要实例化对象的那个对象
        self.age = age
        self.height = height
        self.weight = weight
        self.__money = money

    # 通过内部的方法，去修改私有属性
    def set_money(self, money):
        self.__money = money

    # 通过自定义的方法实现对私有属性赋值与取值
    def get_money(self):
        return self.__money


per = Person("tom", 20, 160, 70, 10000)


# 如果要让内部属性，不被外部直接访问。
# 可以在属性前加2个"__". 在python中在属性前，加__ 那个这个属性就变成了私有属性。


# print(per.__money)  # 内部使用

# per.run()  # 外部使用

# 通过set_money 和get_money两种方法来绕过保护了“__money”给money赋值
per.set_money(10)
print(per.get_money())

# 不能直接访问per.__money 是因为Python解释器的原因，把per.__money变成了
# _Person__money,仍然可以用_Person__money去访问。但是不要去做
# 不同版本还可能不一致

# per._Person__money = 15
# print(per.get_money())

# 在python中 __XX__ 属于特殊变量，可以直接访问。
"""
在Python中 _XXX 变量，外部也是可以访问的。但是按照约定的规则，当我们看见这样的变量时，
意思是“虽然我是可以被访问的，但是请把我视为私有变量。”
"""