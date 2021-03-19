# 队列，先进先出
import collections

# 创建一个队列
queue1 = collections.deque()
print(queue1)

# 进队
queue1.append("a")
print(queue1)
queue1.append("b")
print(queue1)
queue1.append("c")
print(queue1)

# 出队
res1 = queue1.popleft()  # 先进先出
print(res1)
