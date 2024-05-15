from threading import *

class Booking(Thread):
    def __init__(self, nm=""):
        super().__init__()
        self.name=nm
        self.__total=50

    def run(self):
        print("Welcome",self.name,"to INOX multiplex")
        required=int(input("Tell us required tickets "))
        if required<=self.__total:
            self.__total-=required
            print(required,"tickets has issued",self.name)
        else:
            print("Available is",self.__total)

b1=Booking("Suresh")
b2=Booking("Vikas")
b3=Booking("Balaji")

b1.start()
b1.join()
b2.start()
#b2.join()
b3.start()