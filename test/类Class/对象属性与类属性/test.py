# class A:
#     def __add__(self, other):
#         print("A __add__")
#
#     def __radd__(self, other):
#         print("A __radd__")
#
#
# class B:
#     pass
#
#
# a = A()
# b = B()
# a + b
# b + a


class MyClass(object):

    def __init__(self, height):
        self.height = height
        # self.weight = weight

    # 两个对象相加返回一个新的类
    def __add__(self, others):
        return MyClass(self.height + others.height)

    # 两个对象的相减.返回一个新的类
    def __sub__(self, others):
        return MyClass(self.height - others.height)

    # 说一下自己的参数
    def intro(self):
        print("高为", self.height)


def main():
    a = MyClass(height=10)
    a.intro()

    b = MyClass(height=20)
    b.intro()

    c = b - a
    c.intro()

    d = a + b
    d.intro()


if __name__ == '__main__':
    main()
