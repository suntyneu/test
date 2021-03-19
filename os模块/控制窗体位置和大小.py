import win32con
import win32gui
import time
import random  #引用随机数
# 找出窗体的编号 我的电脑窗体
pc_win = win32gui.FindWindow("CabinetWClass", "此电脑")
# 参数1
win32gui.SetWindowPos(pc_win, win32con.HWND_TOPMOST, 100, 100, 800, 600, win32con.SWP_SHOWWINDOW)

while True:
    x = random.randrange(900)
    y = random.randrange(600)
    win32gui.SetWindowPos(pc_win, win32con.HWND_TOPMOST, x, y, 800, 600, win32con.SWP_SHOWWINDOW)
