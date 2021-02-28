# 当 `Python` 解释器 **抛出异常** 时，**最后一行错误信息的第一个单词，就是错误类型**

try:
    # 不能确定能正确执行的代码
    num = int(input("请输入一个整数："))
    result = 8 / num
except ZeroDivisionError:
    print("除零错误！")
except ValueError:
    # 处理代码
    print("请输入正确的整数")

print("-" * 100)
