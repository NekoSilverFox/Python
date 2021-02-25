# 045 - 元组和列表之间的转换

# 使用 tuple() 函数可以把 `能够修改`的列表 转换成 `不能修改`的元组
num_list = [1, 2, 3, 4]
num_tuple = tuple(num_list)

# 使用 list() 函数可以把`不能修改`的元组 转换成 `能够修改`的列表
num_list = list(num_tuple)
