# %load validation_example1.py
class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    # getter
    def quantity_getter(self):
        return self.__quantity

    # setter
    def quantity_setter(self, value):
        if value > 0:
            self.__quantity = value
        else:
            raise ValueError('quantity must be grater than 0')

    quantity = property(quantity_getter, quantity_setter)


apples = Ingredient('apple', 9)
print(apples.quantity)
apples.quantity = -1