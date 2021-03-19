import time


def decorate(func):
    def wrapper(*args, **kwargs):   # {"clazz}:"1904"}
        print("正在校验中....")
        time.sleep(1)
        print("校验完毕....")
        func(*args, **kwargs)

    return wrapper


@decorate
def f1(n):
    print("---------f1-----------------", n)


@decorate
def f2(name, age):
    print("------------------f2-----------", name)


f1(44)
f2("孙铁岩", 18)


@decorate
def f3(students, class1="1905"):
    print("{}班级的学生如下：".format(class1))
    for stu in students:
        print(stu)


students = ["孙铁岩", "sunck", "tom"]
f3(students, class1="1904")
