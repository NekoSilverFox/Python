# 022 - 不可变和可变参数

"""
 【重点】在函数内部，针对参数使用赋值语句，【不会】影响调用参数是传递的实参变量
 解释：https://www.bilibili.com/video/BV1ex411x7Em?p=348
"""

# num 是不可变的，num_list（列表）是可变的。【注意这里的可变指的是数据类型中存放的值可变，不是传递进去改变全局的】
def demo(num, num_list):
    print("Inside the function:")

    # 赋值语句
    num = 2
    num_list = [4, 5, 6]

    print(num)  # 2
    print(num_list)  # [4, 5, 6]

    print("-" * 50)


gl_num = 1
gl_num_list = [1, 2, 3]

demo(gl_num, gl_num_list)

print(gl_num)  # 1
print(gl_num_list)  # [1, 2, 3]
