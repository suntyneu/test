import tkinter
from tree_windows import TreeWindows
from info_windows import InfoWindows

win = tkinter.Tk()
win.title("树状层级结构")
win.geometry("900x400+200+2000")

path = r"/home/sunty/PycharmProjects"
# /Volumes/MAC II/Python Project/test/Tkinter

info_win = InfoWindows(win)
tree_win = TreeWindows(win, path, info_win)

win.mainloop()
