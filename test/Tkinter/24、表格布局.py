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
label4 = tkinter.Label(win, text="gogo", bg="green")

# 表格布局
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)
# 进入消息循环
win.mainloop()
