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

c.same_method()
