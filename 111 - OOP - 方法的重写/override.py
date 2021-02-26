# 当 **父类** 的方法实现不能满足子类需求时，可以对方法进行 **重写(override)**
class Animal:
    def eat(self):
        print("Eat")

    def drink(self):
        print("Drink")

    def run(self):
        print("Run")

    def sleep(self):
        print("Sleep")

# 注意这里的继承语法，直接在 `()` 中指定父类名称就可以
class Dog(Animal):
    def bark(self):
        print("Wof wof wof ~")
    pass


# 继承具有传递性
class XiaoTianQuan(Dog):
    def fly(self):
        print("Xiao Tian Quan can fly")

    # 重写 - Override
    def bark(self):
        print("Ying ying ying")


xtq = XiaoTianQuan()
xtq.eat()
xtq.drink()
xtq.run()
xtq.sleep()

# 如果在子类中，重写了父类方法
# 在使用子类对象调用方法时，会调用子类重写的方法
xtq.bark()