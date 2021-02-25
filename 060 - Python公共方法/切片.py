test_list = [0, 1, 2, 3]
print(test_list[1:3])  # [1, 2]

test_tuple = (0, 1, 2, 3)
print(test_tuple[1:3])  # (1, 2)


# 【重点】不能对字典进行切片！！！
test_dec = {"a": "a", "b": "b"}
# print(test_dec[0::])
