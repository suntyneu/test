"""
用户登录
输入用户名
输入密码
输入验证码————封装一个函数
"""
"""
random.randint(参数1，参数2)

参数1、参数2必须是整数
函数返回参数1和参数2之间的任意整数
"""
import random


def generate_checkcode(n):
    s = "0123456789abcdefghijkmlnABCDEFGHIJKLMN._*&%$#@"
    code = ""
    for i in range(n):
        ran = random.randint(0, len(s) - 1)
        code += s[ran]
    return code


def login():
    username = input('输入用户名:')
    password = input('输入密码:')
    code = generate_checkcode(6)
    print('验证码是：', code)
    code1 = input("输入验证码：")
    # 验证
    if code.lower() == code1.lower():
        # 验证码输入正确
        if username == "sunck" and password == "123":
            print("用户登录成功")
        else:
            print("用户登录错误")

    else:
        print("验证码输入错误")


# 调用
login()
