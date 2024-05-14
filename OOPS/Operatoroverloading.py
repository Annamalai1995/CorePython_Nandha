#normal method
class operator:
    def __init__(self,a):
        self.a=a
        
        print(self.a+self.a)
obj=operator(10)
obj1=operator(20)
print("sum:",obj.a+obj1.a)
#using operatoroverloading
class oper:
    def __init__(self,a):
        self.a=a 
    def __add__(Self,b):
        return Self.a+b.a
        
    

    
o=oper(50)
o1=oper(100)
print("value:",o+o1)

