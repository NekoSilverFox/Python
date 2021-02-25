# 如果想在 Python 中的字符串中使用双引号，可以使用单引号为字符串赋值
str = 'I am "Fox"'
print(str)

for char in str:
    print(char)

# 统计字符串长度
print(len(str))


# 统计小字串(子字符串)出现的`次数`
print(str.count("Fox"))


# 判断子字符串出现的次数
print(str.index("Fox"))
# print(str.index("Foxxx")) 如果子字符串不存在，会报错


# 判断空白字符，制表符，换行也是空白字符
str = "     \t    \n"
print(str.isspace())  # True