import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("400x400+200+20")

lbv = tkinter.StringVar()
# 与browse相似，不支持鼠标按下后移动选中位置
lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbv)
lb.pack()
for item in ["good", "nice", "handsome", "cool", "324234", "SENFALE ADFEWR ADSD"]:
    # 按顺序添加
    lb.insert(tkinter.END, item)

# 打印当前列表中的选项
print(lbv.get())

# 设置选项
lbv.set(("1","2","3"))


# 进入消息循环
win.mainloop()