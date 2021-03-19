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

# 绝对布局
label1.place(x=10, y=10)
label2.place(x=50, y=50)
label3.place(x=100, y=100)

# 进入消息循环
win.mainloop()
