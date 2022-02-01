# class Duck:
#     def fly(self):
#         print("Duck is flying")
#
# class Stork:
#     def fly(self):
#         print("Stork is flying")
#
# class Dog:
#     def run(self):
#         print("Dog is running")
#
#
# instances = [Duck(), Stork(), Dog()]
# for animal in instances:
#     animal.fly()


class CrayonsBox:
    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        print('Getting the len of the crayon box: {}'.format(len(self._crayons)))
        return len(self._crayons)

    def __getitem__(self, index):
        print('getting item with index {}; that is {}'.format(index, self._crayons[index]))

        return self._crayons[index]


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)
