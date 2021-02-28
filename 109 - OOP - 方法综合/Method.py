class Game(object):
    # 【类属性】最高分
    __top_score = 0

    # 【实例属性】记录当前游戏玩家姓名
    def __init__(self, player_name):
        self.player_name = player_name

    # 【静态方法】显示游戏帮助信息
    @staticmethod
    def show_help():
        print("帮助信息：XXXXXXX")

    # 【类方法】显示历史最高分
    @classmethod
    def show_top_score(cls):
        print("历史最高分为：%d" % cls.__top_score)

    # 【实例方法】开始当前玩家的游戏
    def start_game(self):
        print("%s 的游戏开始" % self.player_name)


# 查看帮助信息
Game.show_help()

# 显示历史最高分
Game.show_top_score()

# 创建游戏对象
gamer = Game("Fox")
gamer.start_game()
