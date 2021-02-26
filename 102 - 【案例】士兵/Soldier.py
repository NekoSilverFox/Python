# 102 - 【案例】士兵

class Gun:
    def __init__(self, model):
        self.model = model
        self.num_bullet = 0

    def add_bullet(self, count):
        self.num_bullet += count

    def shoot(self):
        if self.num_bullet > 0:
            self.num_bullet -= 1
            print("Tu tu tu ~")
        else:
            print("[%s] 没有子弹了！" % self.model)


class Soldier:
    # 【重点】如果没有初始值，可以使用 None 关键字
    def __init__(self, name, gun=None):
        self.name = name
        self.gun = gun

    def fire(self):
        if (self.gun == None):
            print("[%s] 没有枪！" % self.name)
            return

        print("[%s] Ypa!!!!!!!" % self.name)
        self.gun.add_bullet(50)
        self.gun.shoot()


ak47 = Gun("Ak-47")

fox = Soldier("Fox")
fox.gun = ak47
fox.fire()
