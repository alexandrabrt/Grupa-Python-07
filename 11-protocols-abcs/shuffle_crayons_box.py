from random import shuffle


class CrayonsBox:
    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    # def __setitem__(self, key, value):
    #     self._crayons[key] = value


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)

# shuffle(crayons_box)
print('>> Before monkey patching')
for crayon in crayons_box:
    print(crayon)


def set_crayon(crayons_collection, position, crayon):
    crayons_collection._crayons[position] = crayon

CrayonsBox.__setitem__ = set_crayon
shuffle(crayons_box)

print('>> After monkey patching')
for crayon in crayons_box:
    print(crayon)

