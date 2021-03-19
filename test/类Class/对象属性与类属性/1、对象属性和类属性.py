class Person(object):
    # 这里的属性实际上属于类属性（用类名来调用）——类属性是用类名来调用的
    # 这个不叫对象属性，__init__的才叫对象属性
    name = "person"

    def __init__(self, name):
        # 对象属性
        self.name = name


"""
实例化对象
格式：对象名 = 类名（参数列表）  没有参数列表，（）也不能省略。
"""
print("类属性是：", Person.name)
per = Person("tom")  # 实例化对象
print(per)
# 对象属性优先级高于类属性

per.name = 1
print("对象属性是：", per.name)
print(Person.name)

# 动态的给对象添加对象属性
per.age = 19  # 只针对当前对象生效，对于类创建的其他对象没有作用。
print(per.age)

# ageper2 = Person("lilei")
# print(per2.age)

# 删除对象name属性，再调用会使用到同名的类属性
del per.name
print(per.name)

"""
注意：以后千万不要将对象属性和类属性重名，因为对象属性会屏蔽掉类属性。
但是删除对象属性后，又能使用类属性了
"""