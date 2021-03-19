import tkinter

# 创建主窗口
win = tkinter.Tk()
# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("600x400+200+20")
label = tkinter.Label(win, text="suntk is a good man", bg="red")
label.pack()


def func(event):
    print(event.x, event.y)


# Enter 鼠标进入时触发
# Leave 鼠标离开时触发
label.bind("<Enter>", func)
# 进入消息循环
win.mainloop()
