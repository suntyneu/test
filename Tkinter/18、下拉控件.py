import tkinter
from tkinter import ttk

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("400x400+200+20")

"""

"""
# 绑定变量
cv = tkinter.StringVar()
com = ttk.Combobox(win, textvariable=cv)
com.pack()

# 设置下拉数据
com["value"] = ("黑龙江", "吉林", "辽宁")

# 设置默认值
com.current(0)     # 设置默认下标

# 绑定事件


def func(event):
    print("改变事件了")
    print(com.get())
    print(cv.get())


com.bind("<<ComboboxSelected>>", func)








# 进入消息循环
win.mainloop()
