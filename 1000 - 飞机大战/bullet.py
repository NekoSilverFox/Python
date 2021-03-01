from plane_sprites import *
PATH_BULLET = "./images/bullet1.png"


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        # 调用父类方法，设置子弹图片，设置攻击速度
        super().__init__(PATH_BULLET, -2)

    def update(self):
        # 调用父类方法，让子弹沿处置方向飞行
        super().update()

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁")