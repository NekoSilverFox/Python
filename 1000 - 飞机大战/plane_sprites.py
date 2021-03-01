import pygame

"""
    1. 封装游戏中所有需要使用的精灵子类
    2. 提供游戏的 相关工具
"""


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的方法
        super().__init__()

        # 定义游戏精灵属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed
