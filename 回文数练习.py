print("请输入一个五位数：")  #12345
num = int(input())

if num // 10000 == num % 10 and num // 1000 % 10 == num // 10 % 10:
    print("是回文数")
else:
    print("不是回文数")
print(num // 10 % 10)
print(num // 1000)
