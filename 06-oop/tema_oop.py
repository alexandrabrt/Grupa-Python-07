import math

class Fractie:

    def __init__(self, numarator, numitor):
        if numitor == 0:
            raise ZeroDivisionError('Numitorul nu poate fi zero!')

        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        if self.numarator == 0:
            return '0'

        if self.numarator == self.numitor:
            return '1'

        if self.numitor == 1:
            return str(self.numarator)

        return f'{self.numarator}/{self.numitor}'

    def __add__(self, fractie):
        new_numarator = self.numarator * fractie.numitor + self.numitor * fractie.numarator
        new_numitor = self.numitor * fractie.numitor
        cel_mai_mare_numitor_comun = math.gcd(new_numarator, new_numitor)

        return Fractie(new_numarator//cel_mai_mare_numitor_comun, new_numitor//cel_mai_mare_numitor_comun)

    def __sub__(self, fractie):
        new_numarator = self.numarator * fractie.numitor - self.numitor * fractie.numarator
        new_numitor = self.numitor * fractie.numitor
        cel_mai_mare_numitor_comun = math.gcd(new_numarator, new_numitor)

        return Fractie(new_numarator//cel_mai_mare_numitor_comun, new_numitor//cel_mai_mare_numitor_comun)

    def inverse(self):
        if self.numarator == 0:
            raise ZeroDivisionError('Numitorul nu poate fi zero!')

        return Fractie(self.numitor, self.numarator)


if __name__ == '__main__':
    x = Fractie(1, 2)
    y = Fractie(1, 2)
    print(x)
    print(y)
    print(x + y)
    print(x - y)
    print(x.inverse())
