# 不同的类型用加法会有不同的解释
class Person(object):
    # name = "运算符重载"

    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, other):
        return Person(self.num1 + other.num1)

    def __str__(self):
        return "num = " + str(self.num1)


per1 = Person(1)
per2 = Person(2)
print(per1 + per2)
# 等同于
print(per1.__add__(per2))

print(per1)
print(per2)
