





"""
while num <= 5:
    list.append(input())
    num += 1
max = 0
sec = 0
# list1.sort()
"""

list1 = [1002341234123143123412344123410, 32420, 503300, 600222220, 223111111111111111110, 7000, 8000, 9000]
if list1[0] > list1[1]:
    max1 = list1[0]
    sec = list1[1]
else:
    max1 = list1[1]
    sec = list1[0]
i = 2
while i < len(list1):
    if max1 < list1[i]:
        sec = max1
        max1 = list1[i]

    if max1 > list1[i] > sec:
        sec = list1[i]
    i += 1
print(len(list1))
print(sec)





