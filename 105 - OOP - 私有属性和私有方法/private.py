# 105 - OOP - 私有属性和私有方法

# 【重点】在属性名或方法名前增加【两个下划线】，定义的就是私有属性或者方法！！！！

class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s 的年龄是 %d" % (self.name, self.age))


Juddy = Women("Juddy")
# print(Juddy.age)
# Juddy.secret()  # 私有方法不允许在外部调用
