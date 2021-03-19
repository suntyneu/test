import math
i = 100
while i <= 999:

    if i == math.pow((i // 100), 3) + math.pow((i // 10 % 10), 3) + math.pow((i % 10), 3):

        print(i)

    i += 1
