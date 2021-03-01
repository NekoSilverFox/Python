"""
游戏主程序
    1. 封装 主游戏类
    2. 创建 游戏对象
    3. 启动游戏
"""

import pygame
from plane_sprites import *
from background import *

# 常量区
WIDTH = 480
HEIGHT = 700
SCREEN_RECT = pygame.Rect(0, 0, WIDTH, HEIGHT)
FRAME_PER_SEC = 60  # 每秒刷新帧率


class PlaneGame(object):
    def __init__(self):
        print("游戏初始化...")

        print("设置游戏窗口中...")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        print("创建游戏时钟中...")
        self.clock = pygame.time.Clock()

        print("调用私有方法，创建精灵和精灵组...")
        self.__creat_sprites()
        pass

    def start_game(self):
        print("游戏开始...")
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)

            # 事件监听
            self.__event_handler()

            # 碰撞检测
            self.__check_collide()

            # 更新/绘制精灵
            self.__update_sprites()

            # 更新显示
            pygame.display.update()
        pass

    def screen(self, wide, height):
        # background1 = pygame.image.load()
        pass

    def clock(self, time):
        pass

    def __creat_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

    # 事件监听
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()  # 使用类名的方式调用静态方法

    # 碰撞检测
    def __check_collide(self):
        pass

    # 更新精灵组
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束...")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 开始游戏
    game.start_game()
