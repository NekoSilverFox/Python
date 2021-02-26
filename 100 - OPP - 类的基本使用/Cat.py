# 100 - OPP - 类的基本使用

class Cat:

    def __init__(self):
        print("这是一个初始化方法")

        # 使用初始化方法，赋默认值
        # self.属性名 = 属性的初始值
        self.name = "汤姆"

    # 注意，类方法的第一个参数，必须是 self
    # 哪一个对象调用的方法，self 就是哪一个对象的引用
    # 不建议使用，如果用户没指定self的话，会报错
    def eat(self):
        print("%s eat fish" % self.name)

    def drink(self):
        print("Cat drink water")


# 使用类名()常见对象的时候，会自动调用方法 __init__
tom = Cat()

tom.name = "Tom"  # 代码中没有name，但可以为 Tom 增加一个 name 属性（不建议使用）

tom.eat()
tom.drink()

print(tom)
print("十进制打印地址：%d" % id(tom))
print("十六进制打印地址：%x" % id(tom))  # 使用 %x 可以打印16进制地址
