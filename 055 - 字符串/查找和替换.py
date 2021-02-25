str = "Hello world"

# 判断是否以指定字符串开始
print(str.startswith("Hell"))  # True
print(str.startswith("hell"))  # False

# 判断是否以指定字符串结束
print(str.endswith("ld"))  # True


# 查找指定字符串
# index 如果指定的字符串不存在，会报错
# find  如果指定的字符串不存在，会返回 `-1`
print(str.find(" wo"))  # 5
print(str.find("123"))  # -1，不存在会返回 `-1`


# 替换字符串
# 【注意】 replace 方法不会修改源字符串的内容，而是返回一个新的字符串！！！！！
print(str.replace("world", "Python"))  # Hello Python
print(str)  # Hello world
