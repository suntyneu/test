"""
思考：如果不同的人编写的模块同名怎么办？

解决：为了解决模块命中冲突，引入按目录来组织模块的方法，成为包

特点：引用了包以后，只要顶层的包不予其他人发生冲突，那么模块都不会与别人发生冲突
"""


# 注意：目录只有包含一个叫做"__init__.py"的文件，才被认作是一个包
# 主要是为了避免一些滥竽充数的名字，基本上目前这个文件中，什么不用写。
import a.sunck
import b.sunck

a.sunck.say_good()  # 目录a下的sunck
b.sunck.say_good()  # 目录b下的sunck

