import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("400x400+200+20")

"""
列表框控件，可以包含1个或者多个文本框
作用：在listbox控件的小窗口显示一个字符串
"""
# 1、创建一个listbox，添加几个元素
lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE)
lb.pack()
for item in ["good", "nice", "cool", "handsome"]:
    lb.insert(tkinter.END, item)

# 在开始添加
lb.insert(tkinter.ACTIVE, "niubi")
# 在末尾添加
lb.insert(tkinter.END, ["boy", "girl"])      # 将列表当成1个元素添加

# 删除 参数1位开始的索引，参数2位结束的索引，如果不制定参数2，则只删除第一个索引的内容
# lb.delete(1, 3)
# lb.delete(1, 3)

# 选中 参数1位开始的索引，参数2位结束的索引，如果不制定参数2，则只选中第一个索引的内容
# lb.select_set(2, 4)
lb.select_set(3)

# 获取到列表中的元素个数
print(lb.size())

# 获取值 参数1位开始的索引，参数2位结束的索引，如果不制定参数2，则获取第一个索引的内容
print(lb.get(2, 5))

# 返回当前选中的索引项
print(lb.curselection())

# 判断一个选型是否被选中
print(lb.selection_includes(3))

# 进入消息循环
win.mainloop()
