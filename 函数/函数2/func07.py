"""
list1 = [3, 6, 9, 4]
# 对list1的元素进行加5操作
"""


def func():
    list1 = [3, 6, 9, 4]

    def inner_func():
        # 对list1的元素进行加5操作
        for index, i in enumerate(list1):
            # 0, 3
            list1[index] = i + 5  # list1 每个下标index下的值i 都加5
        print(type(list1))
        list1.sort()  # .sort 列表自带排序
    inner_func()
    print(list1)


func()
