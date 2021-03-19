"""
try...except...finally
格式：
try：
    语句t
except 错误码 as e:
    语句1

except 错误码 as e:
    语句2

......

finally：
    语句f

作用：语句t 无论是否有错误，都将执行最后的语句f。
"""

try:
    1 / 0
except ZeroDivisionError as e:
    print("除数为0了")
finally:
    print("必须执行我")
