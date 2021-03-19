import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("400x400+200+20")

'''
Label:标签控件，可以显示文本
wraplength 指定text的文本以宽度进行换行
justify 设置换行后的对其方法
anchor 位置：n 北 e东 s南 w西
'''

label = tkinter.Label(win, text="sun is a good man",
                      bg="pink", fg="red",
                      font=("宋体", 20), width=25,
                      height=10, wraplength=70, justify="left")
# 显示出来
label.pack()

# 进入消息循环
win.mainloop()
