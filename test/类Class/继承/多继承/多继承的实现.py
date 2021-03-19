from child import Child


def main():
    c = Child(3000, 100)
    print(c.money, c.face_value)
    c.play()
    c.eat()
    # 注意：父类中方法名相同，默认调用括号中排前面的父类的方法。
    c.func()


if __name__ == "__main__":
    main()
