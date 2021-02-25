# 010 - 局部变量和全局变量

"""
4) 全局变量命名的建议

* 为了避免局部变量和全局变量出现混淆，在定义全局变量时，有些公司会有一些开发要求，例如：
* 全局变量名前应该增加 `g_` 或者 `gl_` 的前缀
"""

num = 10


def demo1():
    print("demo1" + "-" * 50)

    # global num = 2 函数内部不允许这样直接修改全局变量的值

    # 【重点】global 关键字，告诉 Python 解释器 num 是一个全局变量
    global num
    num = 2
    print(num)  # 【全局】2



def demo2():
    # 只是定义了一个局部变量，不会修改到全局变量，只是变量名相同而已
    num = 100
    print(num)


demo1()
demo2()

print("over")
