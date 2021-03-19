import pickle  # 数据持久性模块

mylist = [1, 2, 3, 4, 5, "sunck is a good man"]
path = r"C:\Users\Administrator\PycharmProjects\test\文件读写\file6.txt"
f = open(path, "wb")
pickle.dump(mylist, f)  # 写文件 pickle.dump
f.close()


# 读取 pickle.load
f1 = open(path, "rb")
tem_list = pickle.load(f1)
print(tem_list)
f1.close()

