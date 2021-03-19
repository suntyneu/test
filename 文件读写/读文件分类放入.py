import collections
import os


def work(path):
    # 打开文件
    res_path = r"C:\Users\Administrator\Desktop\邮箱"
    with open(path, "r") as f:
        while True:
            line_info = f.readline()
            if len(line_info) < 6:
                break
            # 邮箱中的字符串
            mail_str = line_info.split()[0]
            # 邮箱类型的目录
            file_type = mail_str.split("@")[1].split(".")[0]
            dir_str = os.path.join(res_path, file_type)
            if not os.path.exists(dir_str):
                # 不存在，创建
                os.mkdir(dir_str)
            file_path = os.path.join(dir_str, file_type + ".txt")
            with open(file_path, "a") as fw:
                fw.write(mail_str+"\n")


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
                # print("目录：", file_name)
            else:
                # print("普通文件：", file_name)
                work(file_abs_path)

get_all_dir(r"D:\aaa")
