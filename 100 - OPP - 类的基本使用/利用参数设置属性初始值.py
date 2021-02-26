# 利用参数设置属性初始值

class Cat:

    def __init__(self, cat_name):
        print("这是一个初始化方法")
        self.name = cat_name
        print("%s is coming~" % self.name)

    def eat(self):
        print("%s is eating fish" % self.name)

    def __del__(self):
        print("%s is dead!" % self.name)


tom = Cat("Tom")
tom.eat()
del tom  # del 关键字可以删除一个方法
print("=" * 50)  # Tom 是一个全局对象
