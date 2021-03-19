import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("400x400+200+20")

"""
数值范围控件
increment 步长，默认为1
values 最好不要与from_=0, to=100, 同时 使用
"""
# sp = tkinter.Spinbox(win, increment=1, values=(0, 2, 4, 6, 8))  # from_ 注意带下划线
# # sp.pack()
def updata():
    print(v.get())

v = tkinter.StringVar()
# 只要值改变就会执行方法
sp = tkinter.Spinbox(win, from_=0, to=100, increment=1, textvariable=v, command=updata)
sp.pack()

# 赋值
v.set(20)
# 取值
print(v.get())












# 进入消息循环
win.mainloop()
