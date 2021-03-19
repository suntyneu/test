# 定义列和属性
class Student:
    name = "sunty"
    age = 18


# 使用类，创建对象
aa = Student()

print(aa.name, aa.age)

"""
class 类名():
    特征：属性
    动作：方法  
"""


# 类方法
"""
特点：
1、定义需要依赖装饰器@classmethod
2、类方法中的参数不是一个对象，而是类
3、类方法中只可以使用类属性，
4、类方法可否使用普通方法 ？  不能

类方法的作用：
因为类方法只能访问类属性和类方法，所以可以在创建对先前，如果需要完成一些动作，
（功能）。
"""


class dog:

    def __init__(self, nickname):
        self.nickname = nickname

    def run(self):
        print("{}在院子里跑着".format(self.nickname))

    @classmethod
    def test(cls):  # cls class
        print(cls)

    def eat(self):
        print("吃饭")
        self.run()      # 类中的方法调用，需要通过self.方法名()

dog.test()


