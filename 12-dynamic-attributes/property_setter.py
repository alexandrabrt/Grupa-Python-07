# %load property_setter.py
class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value > 0:
            self.__quantity = value
        else:
            raise ValueError('quantity must be grater than 0')

apple = Ingredient('apple', 10)
print(apple.name, apple.quantity)
coffee = Ingredient('coffee', -1)
print(coffee.name, coffee.quantity)