import os
import collections


def get_all_dir(path):
    queue = collections.deque()
    # 进队
    queue.append(path)
    while len(queue) != 0:
        # 出队
        dir_path = queue.popleft()
        # 找出所有的文件
        files_list = os.listdir(dir_path)
        for file_name in files_list:
            file_abs_path = os.path.join(dir_path, file_name)
            if os.path.isdir(file_abs_path):
                queue.append(file_abs_path)
                print("目录：", file_name)
            else:
                print("普通文件：", file_name)

get_all_dir(r"D:\电子书\Kindle_Chinese_books_Public\Kindle_Chinese_books_Public")