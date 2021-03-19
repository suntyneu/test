import tkinter

# 创建主窗口
win = tkinter.Tk()
# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("600x400+200+20")


def func(event):
    print("event.char=", event.char)
    print("event.keycode =", event.keycode)


win.bind("<a>", func)
 
# Enter 鼠标进入时触发
# Leave 鼠标离开时触发

# 进入消息循环
win.mainloop()
