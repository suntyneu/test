import win32con
import win32gui
import time

# 找出窗体的编号
rar_win = win32gui.FindWindow("CabinetWClass", "此电脑")
# 隐藏窗体
win32gui.ShowWindow(rar_win, win32con.SW_HIDE)
# 显示窗体
win32gui.ShowWindow(rar_win, win32con.SW_SHOW)
