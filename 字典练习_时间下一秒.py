time_str = input()
# 12:23:50 时间格式
time_list = time_str.split(":")
h = int(time_list[0])
m = int(time_list[1])
s = int(time_list[2])

s += 1
if s == 60:
    m += 1
    s = 0
    if h == 24:
        h = 0

print("%.2d:%.2d:%.2d" % (h, m, s))

