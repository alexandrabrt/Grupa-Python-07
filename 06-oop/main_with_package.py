from animals import Dog, Cat


if __name__ == '__main__':
    my_dog = Dog("Rex")
    print(my_dog.name)
    my_dog.speak()

    my_cat = Cat("Mitzi")
    print(my_cat.name)
    my_cat.speak()