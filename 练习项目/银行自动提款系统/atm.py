# -*- coding: UTF-8 -*-
import random
from card import Card
from user import User


class Atm(object):
    def __init__(self, all_users):
        self.all_user = all_users  # 卡号--用户

    # 开户
    def create_user(self):
        # 目标：向用户字典中添加一对键值对(卡号-用户)
        name = input("请输入您的姓名：")
        id_card = input("请输入与您的身份证号码：")
        phone = input("请输入您的电话号码：")

        prestroe_money = int(input("请输入与预存款金额："))
        if prestroe_money < 0:
            print("输入错误，开户失败.....")
            return -1

        # 验证密码
        one_passwd = input("请设置密码：")
        if not self.check_passwd(one_passwd):
            print("密码错误，开户失败!!!。。。。。。。")
            return -1

        card_str = self.random_card_id()
        card = Card(card_str, one_passwd, prestroe_money)
        user = User(name, id_card, phone, card)

        # 存字典
        self.all_user[card_str] = user
        print("开户成功，请记住卡号(%s)。" % (card_str))

        # card_id = self.random_card_id()
        # print(card_id)

    # 查询
    def search_user_info(self):
        card_num = input("请输入卡号：")
        # 验证是否存在改卡号
        user = self.all_user.get(card_num)
        if not user:
            print("该卡号不存在！查询失败.......")
            return -1

        # 判断是否锁定
        if user.card.card_lock:
            print("改卡已经被锁定，请解锁后再进行其他操作！........")
            return -1

        # 验证密码
        if not self.check_passwd(user.card.card_passwd):
            print("改卡已经被锁定，请解锁后再进行其他操作！........")
            user.card.card_lock = True
            return -1
        print("账号：%s  余额：%d" % (user.card.card_id, user.card.card_money))

    # 取款
    def get_money(self):
        card_num = input("请输入卡号：")
        # 验证是否存在改卡号
        user = self.all_user.get(card_num)
        if not user:
            print("该卡号不存在！查询失败.......")
            return -1

        # 判断是否锁定
        if user.card.card_lock:
            print("改卡已经被锁定，请解锁后再进行其他操作！........")
            return -1

        # 验证密码
        if not self.check_passwd(user.card.card_passwd):
            print("改卡已经被锁定，请解锁后再进行其他操作！........")
            user.card.card_lock = True
            return -1
        print("账号：%s  余额：%d" % (user.card.card_id, user.card.card_money))

        # 开始取款
        money = int(input("请输入取款金额："))
        if money > user.card.card_money:
            print("余额不足！无法取款......")
            return -1
        user.card.card_money -= money
        print("成功取出{}元，余额为{}元。".format(money, user.card.card_money))

    # 存款
    def save_money(self):
        pass

    # 转账
    def transfer_money(self):
        pass

    # 改密
    def change_passwd(self):
        pass

    # 锁定
    def lock_user(self):
        card_num = input("请输入卡号：")
        # 验证是否存在改卡号
        user = self.all_user.get(card_num)
        if not user:
            print("该卡号不存在！锁定失败.......")
            return -1
        if user.card.card_lock:
            print("改卡已经被锁定！！！请解锁后在操作其他功能")
            return -1
        if not self.check_passwd(user.card.card_passwd):
            print("密码输入错误！从新输入")
            return -1
        temp_id_card = input("请输入身份证号码：")
        if temp_id_card != user.id_card:
            print("身份证号码输入错误，锁定失败.......")
            return -1

        # 锁它
        user.card.card_lock = True
        print("锁定成功！")

    # 解锁
    def unlock_user(self):
        card_num = input("请输入卡号：")
        # 验证是否存在改卡号
        user = self.all_user.get(card_num)
        if not user:
            print("该卡号不存在！无法解锁.......")
            return -1

        # 判断是否锁定
        if not user.card.card_lock:
            print("该卡没有被锁定，无需解锁！........")
            return -1

        if not self.check_passwd(user.card.card_passwd):
            print("密码输入错误！解锁失败")
            return -1

        temp_id_card = input("请输入身份证号码：")
        if temp_id_card != user.id_card:
            print("身份证输入错误！！！解锁失败")
            return -1

        # 开始解锁
        user.card.card_lock = False
        print("解锁成功.......")

    # 补卡
    def new_card(self):
        pass

    # 销户
    def kill_user(self):
        pass

    def check_passwd(self, real_passwd):
        for i in range(3):
            temp_passwd = input("请输入密码：")
            if temp_passwd == real_passwd:
                return True
        return False

    def random_card_id(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str += ch
            # 判断是否重复
            if not self.all_user.get(str):  # 取不到就是None； Not none 就是True
                return str
