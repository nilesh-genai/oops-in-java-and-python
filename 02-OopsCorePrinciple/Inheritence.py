class School:
    def __int__(self):
        self.__schoolname ="NPS"

    def printschoolname(self):
        print("School name:" ,self.__schoolname)

class student(School):
    def __int__(self,name):
        super().__int__()
        self.__studentname=name

    def printStudentName(self):
        print("Student name:", self.__studentName)


def main():
    # Create a new student object with the name "Raj"
    student = student("Raj")

    # Print the student's name
    student.printStudentName()

    # Print the school's name
    student.printSchoolName()


# Execute main function
if __name__ == "__main__":
    main()

