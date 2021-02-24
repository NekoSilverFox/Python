# Python 中的列表（List），其实就是其他语言中的数组
name_list = ["Nick", "Wilde", "Juddy"]

# 1. 取值 和 取索引
print(name_list)  # ['Nick', 'Wilde', 'Juddy']
print(name_list[0])

# 根据内容取下标
print(name_list.index("Wilde"))  # 1
# print(name_list.index("Wilde123"))  # ERROR 如果传入的数据不在列表中，会报错


# 修改数据
name_list[0] = "Fox"
print(name_list)


# 向列表中增加数据
name_list.append("Silverfox")  # 追加
name_list.insert(1, "Two")
tmp_list = [1, 2, 3]
name_list.extend(tmp_list)  # 拓展，将其他列表中的内容追加到本列表中
print(name_list)


# 删除
print("原数组：")
print(name_list)

del name_list[0]
print(name_list)  # 【重点】这样可以按下标删除，`del`会使变量从内存中删除

name_list.remove("Two")  # 注意，不是下标。而应该是内容。如果有多个相同的值，删除第一个
print(name_list)

name_list.pop()
print(name_list)

name_list.clear()
print(name_list)


# 列表的长度
name_list = ["Nick", "Wilde", "Juddy"]
print("列表的长度为：%d" % len(name_list))


# 列表中某一元素出现的次数
print("Nick 出现了 %d 次" % name_list.count("Nick"))


# 排序
name_list.sort()
print(name_list)

name_list = ["Nick", "Wilde", "Juddy"]
name_list.sort(reverse=True)  ## 【重点】反转数组，反向排序
print(name_list)
name_list.reverse()
print(name_list)