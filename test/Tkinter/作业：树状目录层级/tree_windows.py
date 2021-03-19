import tkinter
from tkinter import ttk
import os


# path = r"/Volumes/MAC II"
class TreeWindows(tkinter.Frame):

    def __init__(self, master, path, other_win):
        frame = tkinter.Frame(master)
        frame.grid(row=0, column=0)
        self.other_win = other_win
        self.tree = ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.tree.pack()
        # print(os.path.splitext(path))
        temp_path = self.get_last_path(path)
        print(temp_path)
        root = self.tree.insert("", "end", text=self.get_last_path(path),
                                open=True, values=(path))
        self.load_tree(root, path)

        # 滚动条
        self.sy = tkinter.Scrollbar(frame)
        self.sy.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.sy.config(command=self.tree.yview())
        self.tree.config(yscrollcommand=self.sy.set)

        # 绑定事件
        self.tree.bind("<<TreeviewSelect>>", self.func)

    def func(self, event):
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)["text"]
            self.other_win.ev.set(file)
            apath=self.tree.item(sv)["values"]
            print(apath)

    def load_tree(self, parent, parent_path):
        for file_name in os.listdir(parent_path):
            abs_path = os.path.join(parent_path, file_name)
            # 插入树枝
            treey = self.tree.insert(parent, "end", text=self.get_last_path(abs_path),
                                     values=(abs_path))
            # 判断是否是目录
            if os.path.isdir(abs_path):
                self.load_tree(treey, abs_path)

    def get_last_path(self, path):
        path_list = os.path.split(path)
        return path_list[-1]
