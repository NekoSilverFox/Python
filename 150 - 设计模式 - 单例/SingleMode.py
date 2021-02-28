# 150 - 设计模式 - 单例

class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None

    # 是否执行过初始化动作
    init_flag = False


    # 单例模式 - 让初始化动作只执行一次
    def __init__(self):
        # 1.判断是否执行过初始化动作
        # 注意：用类名调用就可以
        if MusicPlayer.init_flag:
            return

        # 如果没有初始化
        print("播放器初始化")
        MusicPlayer.init_flag = True

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否为空对象
        if cls.instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            # 为对象分配空间
            cls.instance = super().__new__(cls)  # 【重点】
            # 创建对象时，new方法会自动被调用
            print("创建对象，分配空间")

        # 3. 返回对象的引用
        return cls.instance


# 创建播放器对象
player = MusicPlayer()
print(player)
