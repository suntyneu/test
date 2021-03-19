str = input()
index = 0
sum = 0
while index < len(str):
    if str[index] >= "0" and str[index] <= "9":
        sum = sum + int(str[index])
    index += 1
print(sum)
