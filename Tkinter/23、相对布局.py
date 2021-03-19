import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("600x400+200+20")

label1 = tkinter.Label(win, text="good", bg="red")
label2 = tkinter.Label(win, text="ok", bg="yellow")
label3 = tkinter.Label(win, text="nice", bg="blue")

# 相对布局 窗体改变对控件有影响
label1.pack(fill=tkinter.Y, side=tkinter.LEFT)
label2.pack(fill=tkinter.Y, side=tkinter.TOP)

# 进入消息循环
win.mainloop()
