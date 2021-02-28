# 150 - 设计模式 - 单例

class MusicPlayer(object):
    def __init__(self):
        print("播放器初始化")


    def __new__(cls, *args, **kwargs):
        # 创建对象时，new方法会自动被调用
        print("创建对象，分配空间")

        # 为对象分配空间
        instance = super().__new__(cls)  # 【重点】

        # 返回对象的引用
        return instance

# 创建播放器对象
player = MusicPlayer()
print(player)