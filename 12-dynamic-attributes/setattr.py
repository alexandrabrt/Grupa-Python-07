import random


class EveryThingYouAskFor:

    def __getattr__(self, field):
        setattr(self, field, random.random())
        attribute_value = getattr(self, field)
        print(f'Value for field: {field} is {attribute_value}')

        return attribute_value


instance = EveryThingYouAskFor()
print(instance.python_class, instance.abcd, instance.qwerty, instance.unicorns)