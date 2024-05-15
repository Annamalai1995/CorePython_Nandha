from threading import *


class House:
    click=[55,20,66,8,1,10]

class Alpha(Thread,House):
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm
    def run(self):
        print("welcome",self.name)
        self.click.sort()
        for x in self.click:print(x)

class Beta(Thread,House):
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm
    def run(self):
        #lk.acquire()
        print("Welcome",self.name)
        pos=int(input("Tell us position to delete"))
        self.click.pop(pos)
        for x in self.click:print(x)
        #lk.release()

#lk=Lock()

a1=Alpha("Annamalai")
a2=Alpha("Sam")
b1=Beta("karthi")
#b2=Beta("Sathish")

a1.start()
a2.start()
b1.start()
#b2.start()