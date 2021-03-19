import random


def generate_random(number):  # 形参：形式上的参数 number=5
    for i in range(number):
        ran = random.randint(1, 20)
        print(ran)


print(generate_random)  # 打印函数内存地址
# 调用：
generate_random(5)   # 实参：实际的参数，具体的值
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
generate_random(8)


def add(a, b):
    result = a + b
    print("和：", result)


add(2, 3)
