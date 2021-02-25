# 021 - 返回多个结果

def demo1():
    val1 = 1
    val2 = "good"
    # return (val1, val2)  # 返回元组，括号可以省略
    return val1, val2  # 返回元组，括号可以省略


# 简单的接受返回值
result = demo1()
print(result)  # (1, 'good')


# 【重点】如果函数返回的类型是元组，同时希望单独处理元组中的元素
# 可以使用多个变量，一次性接受函数的结果
# 注意：使用多个变量接受结果时，变量的个数应该和结果保持一致
gl_val1, gl_val2 = demo1()
print("val1 = %d    val2 = %s" % (gl_val1, gl_val2))  # val1 = 1    val2 = good


# 单独拿一个数据
print(demo1()[0])  # 1
