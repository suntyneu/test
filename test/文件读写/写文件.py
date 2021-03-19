import time
path = r"C:\Users\Administrator\PycharmProjects\test\文件读写\file2.txt"
f2 = open(path, "a+", encoding="utf-8")
"""
如果以 r+、w、w+、a、a+ 模式打开文件，则都可以写入。
需要指出的是，当以 r+、w、w+ 模式打开文件时，
文件指针位于文件开头处；当以 a、a+ 模式打开文件时，文件指针位于文件结尾处。

另外，需要说明的是，当以 w 或 w+ 模式打开文件时，程序会立即清空文件的内容。
"""

# 写文件1、将信息写入缓冲区2、刷新缓冲区，立刻写入文件。而不是被动的等待关闭文件自动刷新
# 缓冲区写入
"""
f.write("sunck is a good man")
f.write("sunty is a good man")
f.flush()

# while 1:
#    f.write("sunck is a good man\n")
#    f.flush(20)
"""
with open(path, "a") as f2:
    f2.write("sunty is super man!\n")
f2.close()
