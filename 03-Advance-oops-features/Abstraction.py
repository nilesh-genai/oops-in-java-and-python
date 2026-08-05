from abc import ABC,abstractmethod


class Car(ABC):
    def start(self):
        print('Hello')

    @abstractmethod
    def horn(self):
        pass

class Bmw(Car):
    def horn(self):
        print('bmw horn plss')

    @staticmethod
    def rave():
        print('raving')

if __name__ == '__main__':
    bmwObj = Bmw()
    bmwObj.horn()
    bmwObj.start()
    Bmw.rave()