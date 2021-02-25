a = [1, 2, 3]

# len 获取长度
print(len(a))

# del 删除某一元素
del (a[0])
print(a)

del (a)
# print(a)  # 提示 a 没有定义


# max 和 min
num = [9, 4, 3, 4, 10, 5, 5, 9]
print(max(num))
print(min(num))

dec = {
    "a": "z",
    "b": "y",
    "c": "x"
}
# 【重点】 如果是字典，只针对 key 进行比较！！！
print(max(dec))  # c
print(min(dec))  # a

# Python 3.X 中取消了 cmp，因为用元素符号 > < == 就可以
print("2" > "1")  # True
print([1, 1, 1] < [1, 2, 2])  # True
print((1, 1, 1) < (1, 2, 2))  # True
# print({"a": "z" < "b": "y"})  # 【重点】不能对字典进行比较！！！！，因为字典没有顺序的概念
