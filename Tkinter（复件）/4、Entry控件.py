import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("400x400+200+20")

'''
输入控件，用于显示简单的文本内容
'''
# 显示密文 show=“*” # e就代表输入框的而对象
entry = tkinter.Entry(win)
entry.pack()

# 绑定变量
e = tkinter.Variable()
# 关键字 textvariable=e e就代表输入框的而对象
entry = tkinter.Entry(win, textvariable=e)
entry.pack()

# 设置值
e.set("sunk is a good!")

# 取值
print(e.get())
print(entry.get())
# 进入消息循环
win.mainloop()
