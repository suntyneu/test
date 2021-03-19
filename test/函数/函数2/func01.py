import random


# 生成10个随机数
def generate_random():
    for i in range(10):
        ran = random.randint(1, 20)
        print(ran)


print(generate_random)    # 打印函数内存地址
# 调用：函数名()
generate_random()
