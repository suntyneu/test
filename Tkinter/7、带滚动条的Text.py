import tkinter

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
# win.geometry("400x400+200+20")

'''

文本控件:用于显示多行文本
'''
# 创建滚动条
scroll = tkinter.Scrollbar()
text = tkinter.Text(win, width=30, height=5)

# side 放到窗体的哪一侧，fill填充
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)

# 关联
scroll.config(command=text.yview())
text.config(yscrollcommand=scroll.set)


str1 = "I am acutely aware that you have not elected me as your President by your ballots," \
       " and so I ask you to confirm me as your President with your prayers." \
       " And I hope that such prayers will also be the first of many." \
       " If you have not chosen me by secret ballot, " \
       "neither have I gained office by any secret promises. " \
       "I have not campaigned either for the Presidency or the Vice Presidency. " \
       "I have not subscribed to any partisan platform. " \
       "I am indebted to no man, and only to one woman " \
       "-- my dear wife -- as I begin this very difficult job."
text.insert(tkinter.INSERT, str1)

# 进入消息循环
win.mainloop()
