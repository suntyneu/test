"""
datetime比time高级，可以理解datetime基于time进行了封装
提供了各种使用函数，datetime的模块接口更直观，更容易调用
datetime : 同时有时间和日期
timedelta ：主要用于计算时间的跨度
tzinfo ： 时区相关
time ：时间
date ：日期

"""

import datetime

# 获取当前时间
d1 = datetime.datetime.now()
print(d1)
print(type(d1))

# 获取指定的时间
d2 = datetime.datetime(1999, 10, 5, 23, 50, 45)
print(d2)

# 将时间转换为字符串
d3 = d1.strftime("%Y-%m-%d %X")
print(d3)

# 格式化字符串转为datetime对象,注意：转换格式要与字符串一致
d4 = datetime.datetime.strptime(d3, "%Y-%m-%d %X")
print(d4)

# 时间间隔
d5 = datetime.datetime(1999, 10, 1, 10, 28, 25, 123456)
d6 = datetime.datetime.now()
d7 = d6 - d5
print("d7=", d7)
print(type(d7))
print(d7.days)  # 间隔天数
print(d7.seconds)  # 间隔天数除外的秒数
