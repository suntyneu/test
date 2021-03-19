import os


def get_all_dir(path):
    stack = []
    stack.append(path)
    # 处理栈，当栈为空结束循环
    while len(stack) != 0:
        dir_path = stack.pop()  # 从栈中取出数据
        file_list = os.listdir(dir_path)  # 目录所有文件
        for file_name in file_list:  # 处理每一个文件，如果是普通文件则打印，目录则将该目录地址压栈
            file_abs_path = os.path.join(dir_path, file_name)  # 拼接目录和文件名,获取最终的文件名
            if os.path.isdir(file_abs_path):
                print("目录：", file_name)
                # 是目录就压栈
                stack.append(file_abs_path)
            else:
                print("文件：", file_name)


get_all_dir(r"D:\电子书\Kindle_Chinese_books_Public\Kindle_Chinese_books_Public")
