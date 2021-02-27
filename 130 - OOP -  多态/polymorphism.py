class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s Dog play" % self.name)


class XTQ(Dog):
    def play(self):
        print("%s XTQ is play" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        print("%s is playing with %s" % (self.name, dog.name))
        dog.play()


# dog = Dog("旺财")
dog = XTQ("旺财")

xiaoming = Person("小明")
xiaoming.play_with_dog(dog)