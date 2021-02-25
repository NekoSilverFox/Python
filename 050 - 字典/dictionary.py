# 字典类似于 map 容器
# key - 键 （是唯一的）
# value - 值
# 使用 {} 定义

person_dic = {
    "name": "Fox",
    "age": 17,
    "sex": "M",
    "job": "students"
}

# 输出顺序和定义顺序是不一致的！！
print(person_dic)


# 取值
print(person_dic["name"])


# 增加 / 修改
person_dic["favorite"] = "qwq"  # 如果 key 不存在，会增加一个键值对
person_dic["age"] = 14  # 如果 key 存在，会修改这个值
print(person_dic)


# 删除
person_dic.pop("sex")  # 【重点】注意：这里的 pop 不是传统意义上的了，要指定键
print(person_dic)


# 统计键值对的数量
print(len(person_dic))


# 合并字典
tmp_dic = {"height": 1.30,
           "age": 15}  # 注意：如果被合并的字典中包含已经存在的键值对时，会覆盖原有值
person_dic.update(tmp_dic)
print(person_dic)


# 循环遍历 【重点】
for key in person_dic:
    print("%s - %s" % (key, person_dic[key]))


# 清空字典
person_dic.clear()
print(person_dic)