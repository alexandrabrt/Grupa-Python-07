def quantity_field(name):
    def quantity_getter(instance):
        return instance.__dict__[name]

    def quantity_setter(instance, value):
        if value > 0:
            instance.__dict__[name] = value
        else:
            raise ValueError(f'{name} must be grater than 0')

    return property(quantity_getter, quantity_setter)


class Ingredient:
    quantity = quantity_field('quantity')
    price = quantity_field('price')

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price