class Person(object):
    def __init__(self, age, name):
        # self.age = age
        # 限制访问
        self.__age = age
        self.__name = name

        # per = Person(18)
        # print(per.age)
        # 属性直接暴露，不安全，没有数据的过滤

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, age):
    #     if age < 0:
    #         age = 0
    #     else:
    #         self.__age = age

    # 使用set和get方法

    # 方法名为受限制变得去掉双下划线
    @property
    def age(self):
        return self.__age

    @age.setter  # 去掉下划线.setter
    def age(self, age):
        if age < 0:
            age = 0
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter  # 去掉下划线.setter
    def name(self, name):
        self.__name = name


per = Person(15, "sunty")
# per.set_age(15)
# print(per.get_age())


per.age = -1100  # 相当于调用 set_age
print(per.age)  # 相当于调用 get_age
per.name = "sunck"
print(per.name)
