list1 = [1, 3, 5, 0, 11]
m = max(list1)
print(m)

list2 = [{"a": 10, "b": 20}, {"a": 13, "b": 20}, {"a": 33, "b": 15}]

m = max(list2, key=lambda x: x["a"])  # 取出字典里键值为a的值作为比较的依据 ，x为传的一个参数，每遍历一下取出个字典

print("list2的最大值是：", m)
