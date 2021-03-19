str1 = "sunty is superman"
str2 = str1[0:10]
print(str2)
num1 = 10
f1 = 10.24533489654
print("num1 = %d\nstr1 = %s\nf1 = %.3f" % (num1, str1, f1))

'''
# 格式化输出 %d %s %d 占位符
\ 转义字符
\n 换行 转义字符
将一些字符转换成有特殊含义的字符。
\\n 显示\n 不换行
\t 制表符 "四个空格，linux默认8个空格"

r 例如print(r"\\\\t\\"),如果字符串中，好多字符需要转义，前加r,表示内部的
字符串默认不转义
'''
print('tom is a \'good\' man')
print("sunty\tgood")
print(r"\\\\t\\")

# eval()
# 功能：将字符串str当成有效的表达式来求值，并返回计算结果。
num2 = eval("123")
print(num2)

# len(str) 返回字符串的长度
print("aa长度")
print(len("tom is"))  # 长度为6

# lower(str) 转换成字符串大写字母为小写字母
str20 = "sunty IS a SpueR"
print(str20.lower())
print("str20 = %s" % str20)

# upper() 转换字符串中小写字母为大写
print(str20.upper())

# swapcase() 转换大写为小写，小写为大写
print(str20.swapcase())

# capitalize 首字母为大写，其余小写。
print(str20.capitalize())

# title() 每个单词首字母大写
print(str20.title())

# character 字符 char
print(str20.center(40, "*"))

# ljust（width[,fiffchar]) 返回指定宽度的字符串，左对齐
print(str20.ljust(40, "%"))

# rjust（width[,fiffchar]) 返回指定宽度的字符串，右对齐
print("------------------------------------")

# zfill(width) 返回一个长度为width的字符串，前面补0
print(str20.zfill(40))


# count(str[,start][,end] 返回字符串中str出现的次数
str21 = "a wsss ssfsff sss ddd sss sss rrrfgssst rsss"
print("str21.countn(sss)", str21.count("sss"))
print(str21.count("sss", 15, len(str21)))

# find(str[,start][,end]) 检查str字符串是否包含在字符串中，可以指定范围
# 得到的是第一次出现的开始下标，没有返回-1

# rfind(str[,start][,end]) 检查str字符串是否包含在字符串中，可以指定范围，从右之左
print(str21.find("sss"))

# index(str, start=0, end=len(str)  rindex() 从右往左找
# 跟find（）一样，只是str不存在的时候回报一个异常。
str21 = "a wsss ssfsff sss ddd sss sss rrrfgssst rsss"
print("str21=", str21.index("sss"))


# lstrip()  截掉左侧指定的字符，默认为空格。 rstrip() 截取右侧字符
print(str21.strip("a"))


# 字符串比较大小：从第一个字符开始比较,谁的ASCII值大，谁就大。相等，比较下一个。
print("azzzzzz" > "m")

# split(str="") 以str为分隔符截取字符串，指定num,则截取num个字符串，
# 剩下的则放在一个字符串中。
str38 = "****adfas**a*fdasd**************afasdf*****sfddasf**"
print("str38=", str38.split("*"))
# ['', '', '', '', 'adfas', '', 'a', 'fdasd', '', '', '', '', '', '', '', '', '', '', '', '', '', 'afasdf', '', '', '', '', 'sfddasf', '', '']
print(str38.split("*", 3))
# 3 表示截取3个 “*”
# ['', '', '', '*adfas**a*fdasd**************afasdf*****sfddasf**']
str39 = "****adfas**a*fdasd***ddfe**sfasfd****ee*sdfs****afasdf*****sfddasf**"
list39 = str39.split("*")
num3 = 0
print(list39)
for s in list39:
    if len(s) > 0:
        num3 += 1
print(num3)

# splistlines([keepends]) 安装（‘\r', '\r\n', '\n')分隔，返回
# keedends = True 会保留换行符
str40 = '''sunck is good man!
sunck is nice man!
sunck is handsome man!
'''
print(str40.splitlines())
print(str40.splitlines(True))


# join(seq) 以指定的字符串，将seq中的元素作为分隔符组合成一个字符串
# 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
list41 = ['sunck', 'is', 'a', 'good', 'man!']
str42 = "@".join(list41)
print(str42)

# max() min()

# replace(oldstr, newstr, count) count是前count个
str44 = "sunck is a good good good man"
str45 = str44.replace("good", "nice")
print(str45)




str47 = "sunck is a good good good man"
t46 = str47.maketrans("go", "65")
print(t46)
str48 = str47.translate(t46)
print(str48)
