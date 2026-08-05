
from abc import ABC,abstractmethod


class Phone(ABC):
    @abstractmethod
    def model(self):
        pass

class Chip(ABC):
    def assembleIphoneChip(self):
        pass

class Iphone(Phone,Chip):
    def model(self):
        print('Iphone 16 Pro')

    def assembleIphoneChip(self):
        print('chip installed')

if __name__ == "__main__":
    Iobj=Iphone()
    Iobj.model()
    Iobj.assembleIphoneChip()