def print_line(char, times):
    """打印当行分割线

    :param char: 分隔的字符
    :param times: 重复的次数
    """
    print(char * times)


def print_lines(char, times):
    """打印多行分割线

    :param char: 分割线使用的字符
    :param times: 分割线重复的次数
    """
    row = 0

    while row < 5:

        print_line(char, times)

        row += 1

name = "冰糖雪狸"