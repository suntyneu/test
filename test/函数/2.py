def outer(func):
    def inter(age):
        if age < 0:
            age = 0
        func(age)
    return inter


@outer
def say(age):
    print("sunck is %d years old" % age)


say(30)
