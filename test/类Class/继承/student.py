from person import Person


class Student(Person):
    def __init__(self, name, age):
        # 调用父类中的__init__
        # super() 函数是用于调用父类(超类)的一个方法。
        super(Student, self).__init__(name, age)
