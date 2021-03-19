import tkinter
from tkinter import ttk

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("400x400+200+20")

"""
框架控件
在屏幕上显示矩形区域，多作为容器控件
"""
frm = tkinter.Frame(win)
frm.pack()

# left
frm_1 = tkinter.Frame(frm)   # 可选参数frm 为 win
tkinter.Label(frm_1, text="左上", bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm_1, text="左下", bg="blue").pack(side=tkinter.TOP)
frm_1.pack(side=tkinter.LEFT)     # 左侧显示

# Right
frm_2 = tkinter.Frame(frm)
tkinter.Label(frm_2, text="左上", bg="red").pack(side=tkinter.TOP)
tkinter.Label(frm_2, text="左下", bg="yellow").pack(side=tkinter.TOP)
frm_2.pack(side=tkinter.RIGHT)     # 右侧侧显示




# 进入消息循环
win.mainloop()
