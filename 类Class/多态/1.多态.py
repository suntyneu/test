"""
多态：一种事务的多种形态
最终目标：人可以喂任何一种动物

"""
from tom import Tom
from jerry import Jerry


tom = Tom("tom")
jerry = Jerry("jerry")

tom.eat()
jerry.eat()

# 思考：再添加100中属性，也都有name属性和吃方法。