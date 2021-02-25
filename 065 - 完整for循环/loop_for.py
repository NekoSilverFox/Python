# 065 - 完整for循环

##############################################################
for num in [1, 2, 3]:
    print(num)

    if num == 2:
        break

else:  # 【重点】当for循环没有完整的遍历完成，else语句就不会执行（例如使用break进行中断）
    print("会执行吗")

print("循环结束")
##############################################################

# 应用场景：
students = [
    {"name": "阿土",
     "age": 20,
     "gender": True,
     "height": 1.7,
     "weight": 75.0},

    {"name": "小美",
     "age": 19,
     "gender": False,
     "height": 1.6,
     "weight": 45.0},
]

find_name = "阿土"

for stu_dict in students:

    print(stu_dict)

    # 判断当前遍历的字典中姓名是否为find_name
    if stu_dict["name"] == find_name:
        print("找到了")

        # 如果已经找到，直接退出循环，就不需要再对后续的数据进行比较
        break

else:
    print("没有找到")

print("循环结束")