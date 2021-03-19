
'''
windows:勾选了pip和add Python.exe to path
Linux Mac 系统自带

'''

"""
安装第三方库（模块），需要知道库（模块）的名字

pillow 非常强大的处理图像的工具库
安装：pip install pillow
如果报错，更新pip——pip install --upgrade pip
"""

# 引入三方库
from PIL import Image
im = Image.open("cim.jpg")
# 查看图片的信息
print(im.format, im.size, im.mode)

# 设置图片的大小
im.thumbnail((150, 100))
# 保存成新图片
im.save("temp.jpg", "JPEG")
