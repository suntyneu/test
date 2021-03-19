"""
当程序遇到问题时，不让程序结束，而越过错误继续向下执行

try......except.......else

格式：
try：
    语句t
except 错误码 as e:
    语句1

except 错误码 as e:
    语句2

......

else：
    语句e

注意：else语句可有可无
作用：用来检测try语句中的错误，从而让except语句捕获到错误信息
    并处理

逻辑：当程序执行到try_except_else语句时
1、如果当try “语句t” 执行出现错误，会匹配第一个错误码，如果
匹配上就会执行相对应的“语句”
2、如果当try“语句t“执行出现错误，没有匹配的异常，错误将会提交到上一层
的try语句。或者到程序的最上层。
3、如果当try“语句t”执行没有出现错误，执行else下的“语句e”
"""
try:
    print(3 / 0)
except ZeroDivisionError as e:
    print("除数为0了")
except NameError as e:
    print("没有该变量")
else:
    print("代码没有问题")
print("**********************")

"""
AttributeError：属性错误，特性引用和赋值失败时会引发属性错误
NameError：试图访问的变量名不存在
SyntaxError：语法错误，代码形式错误
Exception：所有异常的基类，因为所有python异常类都是基类Exception的其中一员，异常都是从基类Exception继承的，并且都在exceptions模块中定义。
IOError：一般常见于打开不存在文件时会引发IOError错误，也可以解理为输出输入错误
KeyError：使用了映射中不存在的关键字（键）时引发的关键字错误
IndexError：索引错误，使用的索引不存在，常索引超出序列范围，什么是索引
TypeError：类型错误，内建操作或是函数应于在了错误类型的对象时会引发类型错误
ZeroDivisonError：除数为0，在用除法操作时，第二个参数为0时引发了该错误
ValueError：值错误，传给对象的参数类型不正确，像是给int()函数传入了字符串数据类型的参数。
"""

# 使用except而不使用任何的错误类型
try:
    print(4 / 0)
except:
    print("程序出现了异常")

# 使用except带着多种异常
try:
    5 / 0
except(NameError, ZeroDivisionError):
    print("出现了NameError, ZeroDivisionError")

# 特殊
# 1、错误其实是class（类），所有的错误都继承自BaseException,
# 所以在捕获的时候，他捕获了该类型的错误，还把子类一网打尽。
# 2、跨越多层调用：main调用func2，func2--func1，func1出现了，
# 这是只要main捕获到了，就可以处理。

print(" # 特殊 ")
def func1(num):
    print(1 / num)
def func2(num):
    func1(num)
def main():
    func2(0)

try:
    main()
except ZeroDivisionError as e:
    print("除数为0")




