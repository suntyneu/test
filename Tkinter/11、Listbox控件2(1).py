import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("400x400+200+20")

# 绑定变量
lbv = tkinter.StringVar()
# 和 BORWSE相似，但不支持鼠标按下后移动选中位置
lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbv)
lb.pack()
for item in ["good", "nice", "cool", "handsome"]:
    lb.insert(tkinter.END, item)

# 打印列列表中的选项
print(lbv.get())


# 绑定事件
def my_print(event):
    print(lb.get(lb.curselection()))     # lb.curselection() 为下标


lb.bind("<Double-Button-1>", my_print)

# 设置选项
# lbv.set(("1", "2", "3"))  # 两层括弧
# print(lbv.get())














# 进入消息循环
win.mainloop()
