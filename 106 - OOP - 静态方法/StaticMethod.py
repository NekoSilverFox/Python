class Dog(object):

    @staticmethod
    def run():

        # 如果这个方法不访问实例属性/类属性，就是用静态方法
        print("Dog is running")

# 通过 `类名.调用静态方法`
Dog.run()