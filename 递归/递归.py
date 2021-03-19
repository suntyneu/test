"""
递归调用：一个函数，调用了自身，称为递归调用
递归函数：一个会调用自身的函数，称为递归函数

凡事循环能干的事，递归都能干——但是不是一般人能写的出来
"""
"""
方式：
1、写出临界条件
2、找出这一次和上一次的关系
3、假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果。


def sum1(n):
    sum = 0
    for x in range(1, n+1):
        sum += x
    return sum
f = sum1(100)
print(f)

"""

# 数入一个数，求1+2+3+4....n的和

"""
1+2+3+4+5
sum2(1) + 2 = sum2（2）
sum2(2) + 3 = sum2（3）
sum2(3) + 4 = sum2（4）
sum2(4) + 5 = sum2（5）
"""
# 用递归来写


def sum2(n):
    if n == 1:
        return 1
    else:
        return n + sum2(n - 1)


res2 = sum2(5)
print("res2，递归=", res2)
