"""
可迭代对象：可以直接作用关于for循环的对象，统称为可迭代对象
Iterable.可以用isinstance()去判断一个对象，是否是Iterable对象。

可以直接作用于for的数据类型，一般分为两种
1、集合类数据类型,如：lis，tuple，dict、set、string
2、是generator，包括生成器和带yield的generator function
"""
from collections import Iterable
print(isinstance([], Iterable))


