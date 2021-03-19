def bb(a, b, *c, **d):
    pass
    print(a, b, c, d)


bb(1, 2)  # 打印结果为：1 2 () {}

bb(1, 2, 3, 4)  # 1 2 (3, 4) {}

bb(1, 2, x=100, y=200)  # 1 2 () {'x': 100, 'y': 200}
"""
注意：只要有关键字就是给**赋值的
* 元祖（） ** 字典{}
"""

bb(1, 2, 3, x=100)  # 1 2 (3,) {'x': 100}


def func(a, *args):
    print(a, args)


func(2, 3, 4, 5)  # 2 (3, 4, 5)
func(2, [1, 2, 3, 4])  # 2, ([1, 2, 3, 4], )
func(2, 3, [1, 2, 3, 4, 5])  # 2 (3, [1, 2, 3, 4, 5])
func(5, 6, (4, 5, 6), 9)  # 5 (6, (4, 5, 6), 9)

