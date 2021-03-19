i = 0
num = 10000
while num <= 99999:
    if num // 10000 == num % 10 and num // 1000 % 10 == num // 10 % 10:
        i += 1
    num += 1
print(i)
