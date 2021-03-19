# -*- coding: UTF-8 -*-
import time


class Admin(object):
    admin = "1"
    passwd = "1"

    def print_admin_view(self):
        print("*************************************************************")
        print("*                                                           *")
        print("*                                                           *")
        print("*                                                           *")
        print("*                                                           *")
        print("*                    欢迎登录银行系统                          *")
        print("*                                                           *")
        print("*                                                           *")
        print("*                                                           *")
        print("*                                                           *")
        print("*                                                           *")
        print("*************************************************************")

    def print_sys_function_view(self):
        print("************************************************************")
        print("*                                                          *")
        print("*        开户（1）             查询（2）                      *")
        print("*        取款（3）             存款（4）                      *")
        print("*        转账（5）             改密（6）                      *")
        print("*        锁定（7）             解锁（8）                      *")
        print("*        补卡（9）             销户（0）                      *")
        print("*                   退出（Q）                                *")
        print("************************************************************")

    def admin_option(self):
        input_admin = input("请输入管理员账号：")
        if self.admin != input_admin:
            print("账号输入有误")
            return -1
        input_passwd = input("请输入管理员密码：")
        if self.passwd != input_passwd:
            print("密码输入错误")
            return -1

        # 执行到这里说明账号密码正确
        print("操作成功，请稍后......")
        time.sleep(0.5)
        return 0
