card_list = []


def printWelcomeInfo():
    """打印欢迎信息

    :return: 无
    """
    star_time = 50
    print("*" * star_time)
    print("欢迎使用【名片管理系统】V1.0\n"
          + "\n"
          + "1. 新建名片\n"
          + "2. 显示全部\n"
          + "3. 查询名片\n"
          + "\n"
          + "0. 退出系统")
    print("*" * star_time)


def userChoise():
    """用户的选择

    :return: 用户选择，如果异常，返回 -1
    """
    return input("请输入功能：")


def makeCard():
    """新建用户名片

    :return: 如果中途退出，返回 -1
    """
    name = input("姓名：")
    while name.isspace() or (len(name) == 0):
        name = input("姓名不能为空！请重新输入！如若想退出，请输入`0`\n"
              + "姓名：")
        if name == "0":
            return -1

    tele = input("电话：")
    sex = input("性别：")

    return {
        "name": name,
        "tele": tele,
        "sex": sex
    }


def pushCard(card):
    """将一个名片，插入到列表中

    :param card: 一个名片
    :return: 无
    """
    card_list.append(card)


def printAllCard():
    """显示全部名片

    :return: 无
    """
    print("-" * 50)
    print("姓名".center(10, " ") + "电话".center(16, " ") + "性别".center(5, " "))
    print("-" * 50)
    for card in card_list:
        print(card["name"].center(10, " ") + card["tele"].center(16, " ") + card["sex"].center(5, " "))
    print("-" * 50)
    print("显示结束！")


def serchCard():
    """查询名片

    :return: 无
    """
    key = input("请输入查询关键字：")
    is_catch = False

    print("-" * 50)
    print("姓名".center(10, " ") + "电话".center(16, " ") + "性别".center(5, " "))
    print("-" * 50)
    for card in card_list:
        if ((card["name"] == key)
                or (card["tele"] == key)
                or (card["sex"] == key)):
            print(card["name"].center(10, " ") + card["tele"].center(16, " ") + card["sex"].center(5, " "))
            is_catch = True
        # else:
        #     print("没有匹配的记录！")
        # TODO 增加修改功能
    print("-" * 50)

    if is_catch == False:
        print("查询结束，未找到相应的记录！")
    else:
        print("查询结束！")
