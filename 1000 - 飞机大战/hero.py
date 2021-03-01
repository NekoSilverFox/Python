import pygame
from plane_sprites import *
from bullet import *

# 英雄发射子弹时间
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class Hero(GameSprite):
    def __init__(self):
        # 调用父类方法，设置image&speed
        super().__init__(PATH_HERO, 0)
        # 设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def fire(self):
        print("Fire!!")
        for i in (0, 1, 2):
            # 创建子弹精灵
            bullet = Bullet()

            # 设置精灵位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 添加精灵
            self.bullets.add(bullet)

    def update(self):
        # 让英雄在水平方向移动
        self.rect.x += self.speed
        # 控制英雄不能移除屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
