path = r"C:\Users\Administrator\PycharmProjects\test\文件读写\file5.txt"
# f2 = open(path, "w", encoding="utf-8")

with open(path, "w", encoding="utf-8")as f1:
    str = "I love python!孙铁岩!"
    f1.write(str)
with open(path, "r", encoding="utf-8", errors="ignore")as f2:
    data = f2.read()
    print(data)
    print(type(data))


# 编码解码方式要一致


with open(path, "ab")as f3:
    str1 = "I love python!孙铁岩...."
    f3.write(str1.encode("utf-8"))
with open(path, "rb")as f4:
    data = f4.read()
    print(data)
    print(type(data))
    new_data = data.decode("utf-8")
    print(new_data)
    print(type(new_data))

# 二进制不带 enconding 和 errors参数
