import sys
import time
import datetime
"""
概述：代码量越来越大，必须分开在不同的文件
    模块相应而生。
我们把很多相似功能的函数分组，分别放到不同的文件中去，
每个文件大致功能可以用文件名来体现。
.py 文件就是一个模块
"""

"""
特点：
1、提高了代码的可维护性
2、提高了代码的复用度，可以别多个地方引用
3、引用其他的模块（内置模块和三方模块和自定义模块）
4、避免函数名和变量名的冲突


print(sys.argv)

for i in sys.argv:
    print(i)

# sys.argv获取命令行参数的列表（终端）
name = sys.argv[1]
age = sys.argv[2]
hoby = sys.argv[3]
print(name, age, hoby)

"""

# 自带查找所需模块路径的列表
print(sys.path)