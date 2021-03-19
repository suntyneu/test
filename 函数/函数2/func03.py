"""
定义一个登录函数

"""
"""
函数体：
判断参数传送过来的usrname,password是否正确，如果正确则登录成功
否则打印登录失败
"""


def login(username, password):
    # 相当于数据库注册的用户名和密码
    uname = "admin123"
    pwd = "112233"
    for i in range(2):
        if uname == username and pwd == password:
            print("登陆成功！")
        else:
            print("登陆失败！")
            username = input("输入用户名:")
            password = input("输入密码:")

    else:
        print("账号锁定")


# 调用：
username = input("输入用户名:")
password = input("输入密码:")
login(username, password)

