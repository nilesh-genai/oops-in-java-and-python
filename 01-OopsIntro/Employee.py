class Employee:
    def __int__(self):
        self.__salary=0
        self.employeeName = ""

    def setSalary(self,sal):
        self.__salary = sal

    def setempname(self,name):
        self.employeeName=name

    def getempname(self):
        return self.employeeName
if __name__ == "__main__":
    obj = Employee()
    obj.setempname("Nilesh")
    print(obj.getempname())



