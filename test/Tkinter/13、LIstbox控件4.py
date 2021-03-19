import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry()

lbv = tkinter.StringVar()

# MULTIPLE 单击多选
lb = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE, listvariable=lbv)
lb.pack()
for item in ["good", "nice", "cool", "handsome", "good", "nice", "cool",
             "good", "nice", "cool", "handsome", "handsome",
             "good", "nice", "cool", "handsome", ]:
    lb.insert(tkinter.END, item)

# 滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
sc['command'] = lb.yview()

# 额外给属性赋值



# 进入消息循环
win.mainloop()
