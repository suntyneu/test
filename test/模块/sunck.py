# 每一个模块都有一个__name__属性，当其值等于__main__时，表明该模块自身在执行。

# 当前文件如果为程序的入口文件，则__name__属性值为__main__时，表明该模块自身在执行，
# 否则引入其他文件。

if __name__ == "__main__":
    print("这是sunck.py文件")
else:
    def say_good():
        print("sunck is a good man")

    def say_nice():
        print("sunck is a nice man")




