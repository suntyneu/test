import os
"""
os:包含了普遍的操作系统的功能

打印操作系统详细的信息，windows不支持
print(os.name)  # 获取操作系统类型nt-windows， posix-Linux、Unix或Mac OS X
f = os.uname()
print(f)

"""
# print(os.environ)  # 获取操作系统中所有环境变量

# f1 = os.environ.get("appdata")
# print(f1)

print(os.curdir)  # 获取当前目录

print(os.getcwd())  # 获取当前工作目录，当前python脚本所在的目录

# 返回指定目录下的所有文件，以列表返回 "目录也是文件"
# print(os.listdir(r"C:\Users\Administrator\PycharmProjects\test"))


# os.mkdir("sunck")  # 在当前目录下建立目录
# os.rmdir("sunck")  # 在当前目录下删除目录


# 获取文件属性
# print("获取文件属性", os.stat("sunck"))

# 重命名
# os.rename("sunck", "kaige")

# 删除文件 os.remove()

# os.system("notepad")  # 运行shell命令
# os.system("mspaint")

# 有些方法存在os模块里，还有些存在于os.path
# 查看当前的绝对路径
print("查看当前的绝对路径", os.path.abspath("."))

# 拼接路径
p1 = r"C:\Users\Administrator\PycharmProjects\test"  # 注意最后不要有“\”
p2 = "os模块"  # 注意，开始不要有 “\”
print("拼接路径：", os.path.join(p1, p2))

# 拆分路径
path2 = r"C:\Users\Administrator\PycharmProjects\test\1.py"
print("拆分路径:", os.path.split(path2), os.path.split(path2))  # 拆分出一个元组


print("获得扩展名 没有为空:", os.path.splitext(path2))  # 获得扩展名 没有为空


# 判断是否是目录
print(os.path.isdir(path2))

# 判断文件是否存在
path3 = r"C:\Users\Administrator\PycharmProjects\test\os模块"
print("判断文件是否存在", os.path.isfile(path3))

# 获得文件大小
print(os.path.getsize(path3))


print("os.path.dirname(path3)", os.path.dirname(path3))
print(os.path.basename(path3))
