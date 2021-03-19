# 可变可变和不可变
# 可变：地址不变里面内容改变 list dict set
# 不可变：只要内容改变，必须改变地址 int str float tuple frozenset

# 函数：
# 增加代码复用度
a = 100
for i in range(a):
    a += 1
print('修改后的a:', a)


def decorate(func):
    def zhuagnxiu(*args, **kwargs):
        func()

        def inner(*args):
            print("我开始装修了")

        print("我装修完事了")
        return inner

    return zhuagnxiu


@decorate(a)
def house(a):
    print("我想装修了")


house(a)
