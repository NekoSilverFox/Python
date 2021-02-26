# 利用参数设置属性初始值

class Cat:

    def __init__(self, cat_name):
        print("这是一个初始化方法")
        self.name = cat_name

    def eat(self):
        print("%s is eating fish" % self.name)


tom = Cat("Tom")
tom.eat()