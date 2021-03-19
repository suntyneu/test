# -*- coding: UTF-8 -*-
"""
人
类目：Person
属性： 姓名 身份证号 电话号码 卡
行为：

卡
类名：Card
属性：卡号 密码 余额

提款机
类目：Atm
属性：
行为：开户 查询 取款 存款 转账 改密 锁定 解锁 补卡 销户 退出


管理员类：
类目：Admin
属性：
行为： 管理员界面 管理员验证 系统功能界面

"""
from admin import Admin
from atm import Atm
import time
import pickle
import os


def main():
    # 存取所以用户的信息

    # 界面对象
    admin = Admin()
    admin.print_admin_view()
    # 用户管理员开机
    # 如果view.admin_login()返回值是-1，程序结束。如果是0就不会执行下去
    if admin.admin_option() == -1:
        return -1

    # 提款机对象
    '''
    
    f = open(file_path, "rb")
    all_users = pickle.load(f)
    atm = Atm(all_users)
    '''
    file_path = os.path.join(os.getcwd(), "a.txt")
    all_users = {}
    atm = Atm(all_users)

    # admin.print_sys_function_view()
    while True:
        admin.print_sys_function_view()
        # 等待用户操作
        option = input("请输入你的操作：")
        if option == "1":
            atm.create_user()
        elif option == "2":
            atm.search_user_info()
        elif option == "3":
            atm.get_money()
        elif option == "4":
            print("存款")
        elif option == "5":
            print("转账")
        elif option == "6":
            print("改密")
        elif option == "7":
            atm.lock_user()
        elif option == "8":
            atm.unlock_user()
        elif option == "9":
            print("补卡")
        elif option == "0":
            print("销户")
        elif option == "q":
            if not admin.admin_option():
                # 讲当前系统中用户信息保存到文件中
                # abs_path = os.getcwdb()        # 获取当前目录觉得路径
                # file_path = os.path.join(os.getcwdb(), "allusers.txt")
                f = open(file_path, "wb")
                pickle.dump(atm.all_user, f)
                f.closed
                print(file_path)
                return -1

        time.sleep(0.5)


if __name__ == "__main__":
    main()
    print(os.getcwd())
