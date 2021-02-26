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
    pass


# 继承具有传递性
class XiaoTianQuan(Dog):
    pass

dog = Dog()
dog.eat()
dog.drink()
dog.run()
dog.sleep()

print("^" * 50)

xtq = XiaoTianQuan()
xtq.eat()
xtq.drink()
xtq.run()
xtq.sleep()
