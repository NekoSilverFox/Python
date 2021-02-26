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

    # 1. **在子类中** **重写** 父类的方法
    # 2. 在需要的位置使用 `super().父类方法` 来调用父类方法的执行
    # 3. 代码其他的位置针对子类的需求，编写 **子类特有的代码实现**
    def bark(self):
        print("Ying ying ying")

        # 注意加括号
        super().bark()

        print("其他奇怪的声音")


xtq = XiaoTianQuan()
xtq.bark()
