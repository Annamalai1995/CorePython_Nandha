class college:
    def getStudentInfo(self):
        self.__rollno=input("Enter Roll Number: ")
        self.__name=input("Enter Name: ")

    def printStudentInfo(self):
        print("Roll Number : ", self.__rollno, "Name : ", self.__name)

class BE(college):
    def getBE(self):
        self.getStudentInfo()
        self.__p = int(input("Enter Physics Marks: "))
        self.__c = int(input("Enter Chem Marks: "))
        self.__m = int(input("Enter Maths Marks: "))

    def printBE(self):
         self.printStudentInfo()
         print("Marks in different Subjects : ", self.__p,self.__c,self.__m)

    def calcTotalMarks (self):
        return(self.__p+self.__m+self.__c)

class Result(BE):
    def getResult(self):
        self.getBE()
        self.__total=self.calcTotalMarks()

    def putResult(self):
        self.printBE()
        print("Total Marks out of 300 : ", self.__total)

college = Result()
college.getResult()
college.putResult()
