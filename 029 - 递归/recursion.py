def demo_recursion(num):
    print(num)

    # 递归的出口很重要
    if num == 1:
        return

    num -= 1
    demo_recursion(num)


#demo_recursion(3)


# 计算 1 + 2 + 3 + ... + num 的结果
def sum_numbers(num):

    if num == 1:
        return 1

    # 数字累加
    tmp = sum_numbers(num - 1)

    return num + tmp

print(sum_numbers(100))