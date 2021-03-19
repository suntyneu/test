
path = r"C:\Users\Administrator\PycharmProjects\test\文件读写\file2.txt"
f = open(path, "r", encoding="utf-8")
list8 = f.readlines(40)
print(list8)
f.close()
