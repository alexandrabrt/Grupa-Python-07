from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod
    def laturi(self):
        pass


class Triunghi(Forma):

    def laturi(self):
        print("Am 3 laturi")


t = Triunghi()
t.laturi()