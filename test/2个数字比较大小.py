print("请输入2个2位数")
num1 = int(input())
num2 = int(input())
if num1 // 10 > num2 // 10:
    print("第一个输入的数字大。")
if num1 // 10 == num2 // 10 and num1 % 10 > num2 % 10:
    print("第一个输入的数字大。")
if num1 // 10 == num2 // 10 and num1 % 10 == num2 % 10:
    print("两个数字相等。")
else:
    print("第二个输入的数字大")
