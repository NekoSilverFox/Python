# 多继承可以让子类对象同时具有多个父类的属性和方法

class A:
    def method_A(self):
        print("Method A")

    def same_method(self):
        print("A === same method")

class B:
    def method_B(self):
        print("Method B")

    def same_method(self):
        print("B === same method")

class C(A, B):
    pass

c = C()
c.method_A()
c.method_B()

# 如果是多个父类中同名方法，调用顺序是通过 Python中的 MRO
"""
* `Python` 中针对 **类** 提供了一个 **内置属性** `__mro__` 可以查看 **方法** 搜索顺序
* MRO 是 `method resolution order`，主要用于 **在多继承时判断 方法、属性 的调用 路径**

* 在搜索方法时，是按照 `__mro__` 的输出结果 **从左至右** 的顺序查找的
* 如果在当前类中 **找到方法，就直接执行，不再搜索**
* 如果 **没有找到，就查找下一个类** 中是否有对应的方法，**如果找到，就直接执行，不再搜索**
* 如果找到最后一个类，还没有找到方法，程序报错
"""
print(C.__mro__)
c.same_method()
