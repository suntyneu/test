import tkinter
from tkinter import ttk

# 创建主窗口
win = tkinter.Tk()

# 创建标题
win.title("sunty")
# 设置大小和位置
win.geometry("600x400+200+20")

"""

"""
tree = ttk.Treeview(win)
tree.pack()

# 添加一级树
tree_f1 = tree.insert("", 0, "中国", text="中国CHN", values=("f1"))
tree_f2 = tree.insert("", 1, "英国", text="英国UK", values=("f2"))
tree_f3 = tree.insert("", 2, "美国", text="美国USA", values=("f3"))

# 添加二级树
tree_f1_1 = tree.insert(tree_f1, 0, "中国黑龙江", text="中国黑龙江", values=("f2_1"))
tree_f1_2 = tree.insert(tree_f1, 1, "中国吉林", text="中国吉林", values=("f2_2"))
tree_f1_3 = tree.insert(tree_f1, 2, "中国辽宁", text="中国辽宁", values=("f2_3"))

tree_f2_1 = tree.insert(tree_f2, 0, "伦敦", text="伦敦", values=("f2_1"))
tree_f2_2 = tree.insert(tree_f2, 1, "开普敦", text="开普敦", values=("f2_2"))
tree_f2_3 = tree.insert(tree_f2, 2, "福特", text="福特", values=("f2_3"))

# 添加三级树
tree_f1_1_1 = tree.insert(tree_f1_1, 0, "哈尔滨", text="哈尔滨", values=("f2_1"))
tree_f1_1_2 = tree.insert(tree_f1_2, 1, "长春", text="长春", values=("f2_2"))
tree_f1_1_3 = tree.insert(tree_f1_3, 2, "盘锦", text="盘锦", values=("f2_3"))




# 进入消息循环
win.mainloop()
