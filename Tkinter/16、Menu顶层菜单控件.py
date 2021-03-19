import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("400x400+200+20")

"""

"""
# 菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)

# 创建一个菜单选项
menu1 = tkinter.Menu(menubar, tearoff=False)


def func():
    print("****************")









for item in ["Python", "c", "c++", "js", "go", "java", "swift", "vb", "pb", "c++","Quit"]:
    if item == "Quit":
        # 添加分割线
        menu1.add_separator()
        menu1.add_command(label=item, command=win.quit)
    else:
        menu1.add_command(label=item, command=func)

# 给菜单选项添加内容
menubar.add_cascade(label="语言", menu=menu1)

menu2 = tkinter.Menu(menubar, tearoff=False)
menu2.add_command(label="red")
menu2.add_command(label="yellow")
menu2.add_command(label="bule")
menubar.add_cascade(label="颜色", menu=menu2)






# 进入消息循环
win.mainloop()
