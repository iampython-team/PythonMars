

class OperatorOverloading:
    def __init__(self,a):
        self.a=a
        print(a)
        
    def __add__(self,other1,other2):
       return self.a+other1.a+other2.a
    
    def __sub__(self,other):
        return self.a-other.a
        

object1=OperatorOverloading(15)
object2=OperatorOverloading(38)
object3=OperatorOverloading(58)
print(object1-object2)
#print(object1+object2+object3)




