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

print("=" * 50)

# 以下三种方法都不能判断小数
num_str = "1.1"
print(num_str)
print(num_str.isdecimal())  # False 只对字符串是不是全是阿拉伯数字（全角数字）做判断
print(num_str.isdigit())  # False 可以对全角数字、(1)、\u00b2 做判断
print(num_str.isnumeric())  # False 还可以对中文数字做判断

print("=" * 50)

num_str = "\u00b2"
print(num_str)
print(num_str.isdecimal())  # False 只对字符串是不是全是阿拉伯数字（全角数字）做判断
print(num_str.isdigit())  # True 可以对全角数字、(1)、\u00b2 做判断
print(num_str.isnumeric())  # True 还可以对中文数字做判断

print("=" * 50)

num_str = "⑴"  # 注意：是 `⑴` 不是，(1)
print(num_str)
print(num_str.isdecimal())  # False 只对字符串是不是全是阿拉伯数字（全角数字）做判断
print(num_str.isdigit())  # True 可以对全角数字、⑴、\u00b2 做判断
print(num_str.isnumeric())  # True 还可以对中文数字做判断

print("=" * 50)

num_str = "一千二百"
print(num_str)
print(num_str.isdecimal())  # False 只对字符串是不是全是阿拉伯数字（全角数字）做判断
print(num_str.isdigit())  # False 可以对全角数字、(1)、\u00b2 做判断
print(num_str.isnumeric())  # True 还可以对中文数字做判断

print("=" * 50)

num_str = "один"
print(num_str)
print(num_str.isdecimal())  # False 只对字符串是不是全是阿拉伯数字（全角数字）做判断
print(num_str.isdigit())  # False 可以对全角数字、(1)、\u00b2 做判断
print(num_str.isnumeric())  # False 还可以对中文数字做判断
