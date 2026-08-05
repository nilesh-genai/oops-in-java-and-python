class calculator:
    
    def add(self,a,b):
        return a+b

class Animal:
    def sound(self):
        print('Animal')


class Child(Animal):
    def sound(self):
        print('Child')

if __name__ == '__main__':
    calObj= calculator()
    res=calObj.add(2,3)
    print(res)
    res1=calObj.add(2.5,3.44)
    print(res1)

    clObj= Child()
    clObj.sound()

