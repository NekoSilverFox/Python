import pygame
from plane_sprites import *  # 不需要输入模块名称
# 游戏的初始化
# 导入并初始化所有 `pygame` 模块，使用其他模块之前，必须先调用 `init` 方法
pygame.init()

# 编写游戏代码
"""
hero_rect = pygame.Rect(0, 0, 470, 700)
print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸 %d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size) # 返回一个元组，长宽
"""

# 创建游戏主窗口
screen = pygame.display.set_mode((470, 700))


# 加载图像数据
background = pygame.image.load("./images/background.png")
# 将图像绘制到指定位置
screen.blit(background, (0, 0))
# 更新屏幕显示
# pygame.display.update()


# 绘制英雄图像
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
# 可以在所有对象都绘制完毕后再调用
pygame.display.update()

# 确定时钟对象
clock = pygame.time.Clock()



# 3.1 定义 rect记录飞机初始位置
hero_rect = pygame.Rect(190, 300, 102, 126)


# 5.1 创建敌机的精灵
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png", 2)
# 5.2 创建建敌机精灵组
enemy_group = pygame.sprite.Group(enemy1, enemy2)






# 游戏循环 --> 意味着游戏正式开始
while True:
    # 设置游戏输出帧率
    clock.tick(60)

    # 4.1 捕获事件，返回的是一个列表
    event_list = pygame.event.get()
    # 4.2 如果有操作再作出响应
    # if len(event_list) > 0:
    #     print(event_list)
    for event in event_list:
        if event.type == pygame.QUIT:
            print("游戏退出.....")
            pygame.quit()  # 卸载所有模块
            exit()  # 终止游戏

    # 3.2 修改飞机位置
    hero_rect.y -= 1
    # 判断飞机位置
    if hero_rect.y <= 0 - hero_rect.height:
        hero_rect.y = 700

    # 3.3 调用blit方法绘制图像
    screen.blit(background, (0, 0))
    screen.blit(hero, hero_rect)

    # 5.3 让精灵组调用两个方法
    enemy_group.update()  # update - 让组中所有精灵更新位置
    enemy_group.draw(screen)  # draw 在 screen 上绘制所有的精灵

    # 3.4 调用update方法更新显示
    pygame.display.update()



# 游戏的退出
# 卸载所有 `pygame` 模块，在游戏结束之前调用！
pygame.quit()
