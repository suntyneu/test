students = {"001": ("蔡徐坤", 21), "002": ("王源", 20), "003": ("王俊凯", 20)}


def print_boy(persons):
    if isinstance(persons, dict):  # 判断是否是字典类型
        values = persons.values()
        print(values)
        for name, age in values:  # 遍历元组的values两个元素
            print('{}的年龄是：{}'.format(name, age))


print_boy(students)


def func(**kwargs):  # key word argument
    print(kwargs)


func(a=1, b="hello", c="tom")  # 装包 {'a': 1, 'b': 'hello', 'c': 'tom'}



print("~~~~~~~~~~~~")


def aa(**kwargs):  # 定义函数放**就是装包
    print(kwargs)


aa(a=1, b="hello", c="tom")  # 装包 {'a': 1, 'b': 'hello', 'c': 'tom'}
# 如果在开发时，已知有一个字典

dirct1 = {"a": 1, "b": 2, "c": 3}
aa(**dict1)   # 拆包 调用函数放**就是拆包
