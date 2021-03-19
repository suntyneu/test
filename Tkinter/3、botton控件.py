import tkinter


def func():
    print("sunck is a good man!")


# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("400x400+200+20")

# command 执行函数func
button1 = tkinter.Button(win, text="请输入密码：", command=func)
button1.pack()

button2 = tkinter.Button(win, text="请输入密码：",
                         command=lambda: print("sunty is a good man!"))
button2.pack()

button2 = tkinter.Button(win, text="退出：",
                         command=lambda: win.quit)
button2.pack()
# 进入消息循环
win.mainloop()
