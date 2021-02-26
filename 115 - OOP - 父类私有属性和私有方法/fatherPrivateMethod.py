# 115 - OOP - 父类私有属性和私有方法

"""
1. 子类对象 【不能】 在自己的方法内部，【直接】 访问 父类的 【私有属性】 或 【私有方法】
2. 子类对象 可以通过 【父类】 的 【公有方法】 【间接】 访问到 【私有属性】 或 【私有方法】
"""

class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def public_A(self):
        print("公有方法 - 包含私有属性 %d %d" % (self.num1, self.__num2))


class B(A):
    def demo(self):
        # 访问父类私有属性
        # print(self.__num2)  ERROR 不能访问

        # 访问父类私有属性
        # self.__test()  ERROR 不能访问

        # 可以通过父类的公有方法，访问父类的私有属性/方法
        self.public_A()

# 创建一个子类对象
b = B()
print(b)

# 在外界不能直接访问对象的私有属性/调用私有方法
# print(b.__num2)
# b.__test()

b.demo()