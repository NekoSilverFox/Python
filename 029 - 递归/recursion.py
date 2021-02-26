def demo_recursion(num):
    print(num)

    # 递归的出口很重要
    if num == 1:
        return
    
    num -= 1
    demo_recursion(num)


demo_recursion(3)