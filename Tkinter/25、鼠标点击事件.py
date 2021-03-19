import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("600x400+200+20")


def func(event):
    print(event.x, event.y)


# <Button-1> 鼠标左键 <Button-3>"鼠标右键 <Button-2>" 中间滚轮
# <Double-Button> 左键双击
button1 = tkinter.Button(win, text="leftmouse button")

# bind  给控件绑定的事件
button1.bind("<Button-3>", func)
button1.pack()

# 进入消息循环
win.mainloop()
