# print(type(int))

# class MyFirstClass:
#     pass
#
# x = MyFirstClass()
# y = MyFirstClass()
# z = MyFirstClass()


# class Dog:
#     legs_no = 4
#
#     def __init__(self, name, legs):
#         self.__name = name
#         self.legs_no = legs
#
#     def my_name(self):
#         return self.name
#
#     def __str__(self):
#         return f"Dog with name {self.name}"
#
#     def change_name(self, name):
#         self.name = name
#
#     @staticmethod
#     def speak():
#         print('Bark Bark!')

# print(Dog.legs_no)
# my_dog = Dog('Rex', 3)
# my_other_dog = Dog('Bella', 2)
# print(my_dog.legs_no)
# print(my_other_dog.legs_no)
#
# print(my_dog.my_name())
# print(my_other_dog.my_name())
#
# my_dog.speak()
# my_other_dog.speak()

# print(my_dog.name)
# my_dog.change_name('Rexy')
# print(my_dog.name)
# print(my_dog)
# print(my_dog.__str__())
# print(my_other_dog)

# my_other_dog._age = 20
# print(my_other_dog._age)
# print(my_other_dog._Dog__name)

# print(dir(my_other_dog))

# class Dog():
#     legs_no = 4
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if name:
#             self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     def speak(self):
#         print('Bark Bark!')
#
# my_dog = Dog('Rex')
# print(my_dog.legs_no)
# print(my_dog.name)
# my_dog.name = "New Rex"
#
# print(my_dog.name)

# del my_dog.name
# print(my_dog.name)

# class Cat():
#     legs_no = 4
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if name:
#             self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     def speak(self):
#         print('Miau Miau!')
#
# my_cat = Cat('Mitzi')
# my_dog = Dog('Rex')

# class QuadrupedAnimal:
#     legs_no = 4
#
#
# class Pet:
#
#     def __init__(self, name):
#         self.__name = name + '_'
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if name:
#             self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# class Dog(QuadrupedAnimal, Pet):
#
#     def __init__(self, name):
#         super().__init__('%' + name)
#
#     def speak(self):
#         print("Bark Bark!")
#
# class Cat(QuadrupedAnimal, Pet):
#
#     def speak(self):
#         print("Miau Miau!")
#
# my_dog = Dog("Rex")
# print(my_dog.name)
# my_dog.speak()
#
# my_cat = Cat("Mitzi")
# print(my_cat.name)
# my_cat.speak()

# 1 1 2 3 5 8 ...
class Fibonacci:

    def __init__(self, n):
        self.n = n
        self.count = 0

    def __iter__(self):
        self.value = 1
        self.prev = 0

        return self

    def __next__(self):
        if self.count < self.n:
            value = self.value
            self.value += self.prev
            self.prev = value
            self.count += 1

            return value
        else:
            raise StopIteration


fibonacci = Fibonacci(1000)
for fib in fibonacci:
    print(fib)
