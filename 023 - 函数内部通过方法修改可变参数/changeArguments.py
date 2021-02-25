# 023 - 函数内部通过方法修改可变参数

"""
如果传递的参数是 **可变类型(比如列表)**，在函数内部，使用 **方法** 修改了数据的内容，**同样会影响到外部的数据**
解释：https://www.bilibili.com/video/BV1ex411x7Em?p=349&spm_id_from=pageDriver
"""
def demo(num_list):
    print("Inside the function:")
    num_list.append(9)  # 调用了列表的方法
    print(num_list)  # [1, 2, 3, 9]
    print("-" * 50)


gl_list = [1, 2, 3]
demo(gl_list)
print(gl_list)  # [1, 2, 3, 9]
