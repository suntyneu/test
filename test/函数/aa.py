number1 = 100
list1 = [1, 1, 2, 3, 5]


def func():
    name = "abc"
    global number1
    number1 += 1
    list1.append(0)
    print(number1,list1)


func()
