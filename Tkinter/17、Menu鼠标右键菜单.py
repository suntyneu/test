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
for item in ["Python", "c", "c++", "js", "go", "java", "swift", "vb", "pb", "c++", "Quit"]:
    if item == "Quit":
        # 添加分割线
        menu1.add_separator()
        menu1.add_command(label=item)
    else:
        menu1.add_command(label=item)

menubar.add_cascade(label="语言", menu=menu1)


def show_menu(event):
    menubar.post(event.x_root, event.y_root)


win.bind("<Button-3>", show_menu)

# 进入消息循环
win.mainloop()
