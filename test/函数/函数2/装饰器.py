"""
加入购物车，付款，修改收货地址
判断用户的登录状态

"""


def func(number):
    a = 100

    def inner_func():
        nonlocal a  # nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
        nonlocal number
        number += 1
        for i in range(number):
            a += 1
        print('修改后的a:', a)

    return inner_func


f = func(5)
f()  # 接取返回值 inner_func() ,调用他这个函才会执行

# 函数作为参数
a = 50
func(50)
f1 = func(a)
print(f1)
f1()
