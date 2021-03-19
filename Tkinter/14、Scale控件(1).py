import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("400x400+200+20")

"""
供用户通过拖拽指示器改变变量的值，可以水平和竖直
tkinter.HORIZONTAL  水平
tkinter.VERTICAL    竖直
length=200 水平时表示宽度，竖直时为高度
tickinterval 表示该值得倍数
"""
scale1 = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, tickinterval=10, length=200)  # from_ 后面加下划线
scale1.pack()

# scale2 = tkinter.Scale(win, from_=0, to=100, orient=tkinter.VERTICAL)   # from_ 后面加下划线
# scale2.pack()


# 设置值
scale1.set(20)


# 取值
def show_num():
    print(scale1.get())


tkinter.Button(win, text="按钮", command=show_num).pack()

# 进入消息循环
win.mainloop()
