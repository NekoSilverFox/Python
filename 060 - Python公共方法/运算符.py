# 重复
print([1, 5] * 5)
# 字典不支持重复


# 拼接
print("hello" + " " + "python")
print((1, 2) + (3, 4))

tmp_list = [1, 2]
tmp_list.extend([3, 4])
print(tmp_list)  # extend 会拓展到列表的末尾

tmp_list.append([8, 9])
# 【重点】append 会把列表参数当成一个元素，再添加到列表中
print(tmp_list)  # [1, 2, 3, 4, [8, 9]]


# 判断是否存在，对字典时只能对 key 键进行操作
print("a" in ["b", "c", "a"])  # True
print("a" in "asdffe")  # True
print("a" in {"a": "1", "b": "2"})  # True
print("1" in {"a": "1", "b": "2"})  # False

# not in 代表不存在
print("z" not in "asdffe")  # True
