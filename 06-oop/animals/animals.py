class QuadrupedAnimal:
    legs_no = 4


class Pet:

    def __init__(self, name):
        self.__name = name + '_'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name:
            self.__name = name

    @name.deleter
    def name(self):
        del self.__name


class Dog(QuadrupedAnimal, Pet):

    def __init__(self, name):
        super().__init__('%' + name)

    def speak(self):
        print("Bark Bark!")


class Cat(QuadrupedAnimal, Pet):

    def speak(self):
        print("Miau Miau!")