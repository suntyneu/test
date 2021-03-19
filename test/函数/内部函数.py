# 内部函数


def func():
    # 声明变量
    n = 100  # 局部变量
    list1 = [6, 5, 1, 2, 3, 4]

    # 内部函数
    def inner_func():
        for index, i in enumerate(list1):
            list1[index] = i + 5
            print(list1)
            list1.sort()

    return inner_func


f = func()
f()
