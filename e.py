list27 = [100, 200, 300, 40000, 500, 600, 800, 900, 1341, 1111]

max = 0
sec = 0
if list27[0] > list27[1]:
    max = list27[0]
    sec = list27[1]
else:
    max = list27[1]
    sec = list27[0]
index = 2
while index < len(list27):
    if list27[index] > max:
        sec = max
        max = list27[index]
    index += 1
print(len(list27))
print(sec)
