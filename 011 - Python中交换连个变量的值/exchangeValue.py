# 011 - Python中交换变量的值

a = 1
b = 2
a, b = (b, a)  # 等号右边是一个元组，括号可省略
print(a)  # 2
print(b)  # 1

c = 3
a, b, c = c, b, a
print(a)  # 3
print(b)  # 1
print(c)  # 2