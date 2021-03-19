from types import MethodType


class Person(object):
    __slots__ = ("name", "age")                                      # 关键字 __slots__


per = Person()

# 动态添加属性，这体现了动态语言的特点（灵活）
per.name = "tom"
print(per.name)


# 给对象添加属性
def say(self):
    print("my name is " + self.name)


per.speak = MethodType(say, per)
per.speak()

# 思考：如果我们想要限制实例的属性怎么办?
# 比如说，只允许给对象添加nama,age ,height,weight属性

# 解决:"定义类的时候，定义一个特殊的属性__slots__,可以限制"
