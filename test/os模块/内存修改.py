
import win32process
import win32con
import win32gui
import win32api
import ctypes

Process_ALL_ACCESS = (0X000F0000 | 0X00100000 | 0XFFF)

# 找窗体
win = win32gui.FindWindow()