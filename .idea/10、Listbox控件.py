import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("400x400+200+20")
'''
列表框控件，可以包含一个或者多个文本框
作用：在Listbox控件小窗口显示一个小字符串。
'''
# 1、创建一个listbox，添加几个元素
lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE)
lb.pack()
for item in ["good", "nice", "handsome", "cool", "324234", "SENFALE ADFEWR ADSD"]:
    # 按顺序添加
    lb.insert(tkinter.END, item)

# 在开始添加
lb.insert(tkinter.ACTIVE, "好看")
lb.insert(tkinter.END, ["好好学习", "天天向上"])

# 删除 参数1为开始的索引，参数2为结束的索引，不指定参数2，则删除第一个索引的内容。
# lb.delete(0, 3)
# lb.delete(1)

# 选中
# 选中 参数1为开始的索引，参数2为结束的索引，不指定参数2，则选中第一个索引的内容。
lb.select_set(2, 4)
# lb.select_set(6)

# 取消选中
# 取消选中 参数1为开始的索引，参数2为结束的索引，不指定参数2，则选中第一个索引的内容。
# lb.select_clear(3,4)

# 获取列表中元素的个数
# print(lb.size())

# 从列表中取值
# 参数1为开始的索引，参数2为结束的索引，不指定参数2，则选中第一个索引的内容。
# print(lb.get(2,4))

# 返回当前的索引项，不是item元素
print(lb.curselection())

# 判断 一个选项是不是被选中
print(lb.select_includes(2))
print(lb.select_includes(4))


# 进入消息循环
win.mainloop()
