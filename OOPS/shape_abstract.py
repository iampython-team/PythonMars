from abc import ABC, abstractmethod, abstractstaticmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    def show(self):
        print("in show method")
    
class Traingle(Shape):
    def area(self,breadth,height):
       pass
    
    
T=Traingle()
r=T.area(10,10)
print(r)



# abc - ABC and abstarctmethod 
# class must be inherited from ABC 
# class atleast contains one abstract method 
# abstract method is declared and not implemented 

# new class is inherited from abstract class, that must be implemented the abstract methods 

# we cannot creat an object for abstract class  