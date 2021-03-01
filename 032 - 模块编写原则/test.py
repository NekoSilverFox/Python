def say():
    print("Hello in function")


print("Hello")
say()


# 因为导入文件时，文件中所有没有缩进的代码都会被执行，所以应该这么编写测试代码
def main():
    print("这是一段测试代码")

# 根据 __name__ 判断是否执行下方代码
if __name__ == '__main__':
    main()
