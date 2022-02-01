class QuantityField:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')

class Ingredient:
    quantity = QuantityField('quantity')
    price = QuantityField('price')

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price