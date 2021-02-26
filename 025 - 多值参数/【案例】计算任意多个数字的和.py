"""
**需求**

1. 定义一个函数 `sum_numbers`，可以接收的 **任意多个整数**
2. 功能要求：将传递的 **所有数字累加** 并且返回累加结果
"""


def sum_numbers(*args):
    result = 0
    for num in args:
        result += num
    return result


print(sum_numbers(1, 2, 3, 4, 5))
