# 格式化字符串后面的 `()` 本质上就是元组

print("%s 的年龄是：%d，身高是：%.2f" % ("Fox", 17, 1.65))

info_tuple = ("Fox", 17, 1.65)
print("%s 的年龄是：%d，身高是：%.2f" % info_tuple)

info_str = "%s 的年龄是：%d，身高是：%.2f" % info_tuple
print(info_str)
