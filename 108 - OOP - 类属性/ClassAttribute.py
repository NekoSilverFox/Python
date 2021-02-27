# Class attribute

class Tool(object):

    # 使用赋值语句定义类属性，记录工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值 +1
        Tool.count += 1


tool1 = Tool("tool1")
print(Tool.count)  # 建议使用类名获取类的属性
                # 原因：https://www.bilibili.com/video/BV1ex411x7Em?p=411&spm_id_from=pageDriver

tool2 = Tool("tool2")
print(Tool.count)

tool3 = Tool("tool3")
print(Tool.count)