str_num = "0123456789"

print(str_num[2:6])  # 注意：不包含最后一个字符
print(str_num[2:])  # 切片到最后一个字符
print(str_num[:6])  # 截取0~5
print(str_num[:])  # 截取完整字符串
print(str_num[::1])  # 每隔一个切一刀
print(str_num[1::2])  # 从一开始，每隔一个切一刀
print(str_num[2:-1])  # 从2开始，到倒数-1个
print(str_num[-2:])  # 截取末尾两个字符
print(str_num[-1::-1])  # 字符串逆序