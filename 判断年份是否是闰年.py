print("请输入一个年份:")
num = int(input())
if num % 400 == 0 or (num % 4 == 0 and num % 100 != 0):
    print(num, "年，是闰年")
else:
    print(num, "年，不是闰年")
