 # Encapsulation

class Mobile:
    __model=""
    __price=0.0
    __ram=0
    __internal=0
    def setModel(self, mod=""):self.__model=mod
    def getModel(self):return self.__model
    def setPrice(self, pri=""):self.__price=pri
    def getPrice(self):return self.__price
    def setRam(self, ra=""):self.__ram=ra
    def getRam(self):return self.__ram
    def setInternal(self, inte=""):self.__internal=inte
    def getInternal(self):return self.__internal


mob1=Mobile()
mob1.setModel("Iphone 13")
mob1.setPrice(73000)
mob1.setRam(128)
mob1.setInternal(128)
print(mob1.getModel(),mob1.getPrice(),mob1.getRam(),mob1.getInternal())


mob2=Mobile()
mob2.setRam(12)
mob2.setModel("One plus 10R")
mob2.setInternal(256)
mob2.setPrice(45000)
print(mob2.getModel(),mob2.getPrice(),mob2.getRam(),mob2.getInternal())