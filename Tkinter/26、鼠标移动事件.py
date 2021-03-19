import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("600x400+200+20")

label = tkinter.Label(win, text="sunck is a good man")
label.pack()


def func(event):
    print(event.x, event.y)


label.bind("<B1-Motion>", func)

# 进入消息循环
win.mainloop()
