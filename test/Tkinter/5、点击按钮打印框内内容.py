import tkinter

# 创建主窗口
win = tkinter.Tk()


def show_info():
    print(entry.get())


# 创建标题
win.title("点击打印框内的内容")
# 设置大小和位置
win.geometry("400x400+200+20")
entry = tkinter.Entry(win)
entry.pack()
button = tkinter.Button(win, text="start", command=show_info)
button.pack()

# 进入消息循环
win.mainloop()
