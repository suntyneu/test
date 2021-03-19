
def print99():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("%d x %d = %d" % (j, i, j * i), end=" ")
        print("")


print99()




"""
def word_count(str):
    count = 0
    word_list = str.split(" ")
    for word in word_list:
        if len(word) > 0:
            count += 1
        return count
res = word_count("sunck is a good man")
if res >= t:
    print("right")
else:
    print("aaa")



res = word_count("sunck is a good man")
if res >= t:
    print("right")
else:
    print("aaa")

def printsxh():
    sxhlist = []
    for num in range(100, 1000):
        a = num % 10
        b = num // 10 % 10
        c = num // 100

        if num == a**3 + b**3 + c**3:
            sxhlist.append(num)
    return sxhlist


l = printsxh()
printsxh(l)

"""