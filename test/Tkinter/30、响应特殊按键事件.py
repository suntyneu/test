import tkinter

# 创建主窗口
win = tkinter.Tk()
# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("600x400+200+20")

# <key> 响应所有的按键
label = tkinter.Label(win, text="suntk is a good man", bg="red")

# 设置焦点  可以是win
label.focus_set()
label.pack()


def func(event):
    print("event.char=", event.char)
    print("event.keycode =", event.keycode)


# Enter 鼠标进入时触发
# Leave 鼠标离开时触发
label.bind("<Shift_L>", func)
# 进入消息循环
win.mainloop()
