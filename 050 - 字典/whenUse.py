# 使用 **多个键值对**，存储 **描述一个 `物体` 的相关信息** —— 描述更复杂的数据信息
# 将 **多个字典** 放在 **一个列表** 中，再进行遍历，在循环体内部针对每一个字典进行 **相同的处理**

card_list = [
    {"name": "Fox",
     "QQ": 123456,
     "phone": 10086},
    {"name": "Silverfox",
     "QQ": 654321,
     "phone": 10010},
]

for card_info in card_list:
    print(card_info)

for person in card_list:
    for key in person:
        print("%s - %s" % (key, person[key]))
    print("*" * 50)
