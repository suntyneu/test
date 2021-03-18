import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("400x400+200+20")


def update():
    print(r.get())

r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win, text="one", value=1, variable=r, command=update)
radio1.pack()
radio2 = tkinter.Radiobutton(win, text="two", value=2, variable=r, command=update)
radio2.pack()

# 进入消息循环
win.mainloop()