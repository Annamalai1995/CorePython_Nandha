# Constructor:def __inti__

class Account:

    #constructor
    def __init__(self,name="",num=0,bal=0.0):
        print("Constructor called")
        self.__holder=name
        self.__accNum=num
        self.__accBal=bal

    def __add__(self, other):
        self.__accBal+=other
        print(other,"credited ",self.__accNum)
    def __sub__(self, other):
        if self.__accBal>=other:
            self.__accBal-=other
            print(other,"debited ",self.__accNum)
        else:
            print(self.__accNum," insufficient balance")


    def __str__(self):
        return self.__holder+" "+str(self.__accNum)+" "+str(self.__accBal)+"\n"


    def setHolder(self,name=""):self.__holder=name
    def getHolder(self):return self.__holder
    def setAccNum(self,num=0):self.__accNum=num
    def getAccNum(self):return self.__accNum
    def setAccBal(self,bal=0.0):self.__accBal=bal
    def getAccBal(self):return self.__accBal


acc1=Account()
acc1.setAccNum(789456123)
acc1.setAccBal(4500.5)
acc1.setHolder("priya")
print(acc1)
acc1+5000
print(acc1)

acc2=Account("Gowthami",14578923,7800.5)
print(acc2.getAccBal())