"""
读文件
过程：
1、打开文件
2、读文件内容
3、关闭文件

"""

"""
1、打开文件
open(path, flag[,encoding][,errors])
path:要打开文件的路径
flag:打开方式
r   以只读的方式打开文件，文件的描述符放在文件的开头
rb  以二进制格式打开文件，用于只读，文件的描述符放在文件的开头
r+  打开一个文件可以读写，文件描述符放在开头
w   打开一个文件只用于写入，如果该文件已经存在，会覆盖；不存在则创建一个新文件。
wb  打开一个文件只用于写入二进制，如果该文件已经存在，会覆盖；不存在则创建一个新文件。
w+  打开一个文件只用于读写，如果该文件已经存在，会覆盖；不存在则创建一个新文件。
a   打开一个文件用于追加，如果该文件已经存在，文件描述符将会放在文件末尾。
a+  
encoding:编码方式
errors:错误处理

2、读文件
读取指定字符数，默认全部。
3、关闭文件
"""
path = r"C:\Users\Administrator\PycharmProjects\test\文件读写\file1.txt"
f = open(path, "r", encoding="utf-8")
# str1 = f.read()
# print(str1)

str2 = f.read(25)
print("*", str2, "*")
f.close()

# 3、读取整行，包括“\n”
print("读取整行，包括“\\n”")
path = r"C:\Users\Administrator\PycharmProjects\test\文件读写\file1.txt"
f = open(path, "r", encoding="utf-8")
str4 = f.readline()
print(str4)
f.close()


# 4、读取指定字符数
# str6 = f.readline(10)

# 5、读取所有行，并返回列表 size代表字符数,返回一个列表
#list7 = f.readlines(size)
#print(list7)


print("6")
path = r"C:\Users\Administrator\PycharmProjects\test\文件读写\file2.txt"
f = open(path, "r", encoding="utf-8")
list8 = f.readlines()
print(list8)
# f.close()

# 修改描述符的位置
print("# 修改描述符的位置")
f.seek(10)
str9 = f.read()
print(str9)

# 一个完整的过程
print("一个完整的过程 ")
try:
    f1 = open(path, "r", encoding="utf-8")
    print(f1.read())
finally:
    if f1:
        f1.close()

print("# 最简单的写法 with 自动把文件关上")
# 最简单的写法 with 自动把文件关上
# errors="ignore" 忽略错误继续执行
with open(path, "r", encoding="utf-8", errors="ignore") as f2:
    print(f2.read())
