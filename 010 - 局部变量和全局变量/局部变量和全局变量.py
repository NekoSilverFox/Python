# 010 - 局部变量和全局变量

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
