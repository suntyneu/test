import calendar
"""
日历模块
"""
# 返回某年某月日历
print(calendar.month(1982, 2))

# 返回某年的日历
print(calendar.calendar(2021))

# 判断是否闰年，返回True，否则返回False
print(calendar.isleap(2000))

# 返回某个月的weekday的第一天（日历表前面空几天）和这个月所有的天数
print(calendar.monthrange(2021, 2))

# 返回某个月以每一周为元素的列表 （前后空于用0添加）
print(calendar.monthcalendar(2021, 2))

