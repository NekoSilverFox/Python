class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f\n剩余面积：%.2f\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加：%s" % item)

        if item.area <= self.free_area:
            self.free_area -= item.area
            self.item_list.append(item.name)
            print("%s添加完成，剩余面积：%.2f" % (item.name, self.free_area))
        else:
            print("房屋剩余面积不足！%s 添加失败！" % item.name)


# 1. 创建家具
bed = HouseItem("席梦思", 40)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)

# 创建房子
my_hose = House("两室一厅", 60)
print("-" * 50)
print(my_hose)
print("-" * 50)
my_hose.add_item(bed)
my_hose.add_item(chest)
my_hose.add_item(table)
print("-" * 50)
print(my_hose)
