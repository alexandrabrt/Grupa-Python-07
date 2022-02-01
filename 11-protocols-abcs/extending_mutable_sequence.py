from collections.abc import MutableSequence

class CrayonsBox(MutableSequence):
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
