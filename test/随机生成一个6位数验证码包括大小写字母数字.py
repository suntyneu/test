import random
str = ""
for i in range(6):
    ty = random.randrange(3)
    if ty == 0:
        # 随机生成一个大写字母
        ch = chr(random.randrange(ord('A'), ord('Z') + 1))
        str += ch
    elif ty == 1:
        # 随机生成一个小写字母
        ch = chr(random.randrange(ord('a'), ord('z') + 1))
        str += ch
    else:
        # 随机生成一个数字
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
print(str)
