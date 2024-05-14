# Hierarchy inheritance:
from array import *

class Stocks:
    products=array('i')
    def show(self):print("Products are: ",self.products)

class Jaysurya(Stocks):
    def __init__(self,hey):
        self.products=array('i')
        self.products.extend(hey)
    def search(self):
        budget=int(input("Enter the price  search:"))
        for x in self.products:
            if x<=budget:print(x)
class Reliance(Stocks):
    def __init__(self,hai):
        self.products = array('i')
        self.products.extend(hai)
    def getByPosition(self,start,stop):
        print(self.products[start:stop])

j=Jaysurya([5000,300,800,780,150])
r=Reliance([100,200,300,400,500,600,800,1000])

j.search()

r.getByPosition(0,4)
r.show()
j.show()
