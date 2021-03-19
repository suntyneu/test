# 模拟栈结构 先进后出

stack1 = []

# 压栈（向栈里存数据）
stack1.append("a")
print(stack1)
stack1.append("b")
print(stack1)
stack1.append("c")
print(stack1)

# 出栈（在栈里取数据）
res = stack1.pop()
print(res)
print(stack1)
res = stack1.pop()
print(res)
print(stack1)
res = stack1.pop()
print(res)
print(stack1)
