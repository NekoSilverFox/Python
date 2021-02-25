import cards_tools

while True:
    cards_tools.printWelcomeInfo()

    choise = cards_tools.userChoise()
    if choise == "1":
        card = cards_tools.makeCard()
        if card == -1:
            continue
        cards_tools.pushCard(card)
    elif choise == "2":
        cards_tools.printAllCard()
    elif choise == "3":
        cards_tools.serchCard()
    elif choise == "0":
        print("程序退出！")
        exit()
    else:
        print("未知的指令！请重新输入：")
        continue

print("程序异常退出！")
