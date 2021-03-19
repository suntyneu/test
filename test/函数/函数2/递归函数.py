"""
递归函数：

普通函数： def func（）
            pass
匿名函数： lambda 参数：返回值

递归函数：函数自己调用自己

特点：
1、
"""

# 求一个列表累加和
"""
1 2 3 4 5
sum(1) = 1
sum(2) = sum(1) + 2
sum(3) = sum(2) + 3

"""


def sum(n):  # 1~n
    if n == 0:
        return 0
    else:
        return sum(n - 1) + n


f = sum(100)
print(f)
