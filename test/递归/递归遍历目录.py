import os


def get_all_dir(path, sp=""):  # 定义一个变量sp 空格用
    file_list = os.listdir(path)   # 获取path下所有目录
    #  print(file_list)
    sp += "  "
    for file_name in file_list:   # 处理每一个文件
        file_abs_path = os.path.join(path, file_name)  # 赋值 绝对路径
        if os.path.isdir(file_abs_path):  # 判断是否是目录（要用绝对路径）
            print(sp, "目录:", file_name)
            get_all_dir(file_abs_path, sp)
        else:
            print(sp, "普通文件:", file_name)







get_all_dir(r"D:\电子书\Kindle_Chinese_books_Public\Kindle_Chinese_books_Public")
