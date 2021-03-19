str39 = "****adfas**a*fdasd***ddfe**sfasfd****ee*sdfs****afasdf*****sfddasf**"
list39 = str39.split("*")
num3 = 0
print(list39)
for s in list39:
    if len(s) > 0:
        num3 += 1
print(num3)
