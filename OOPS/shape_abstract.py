from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    def show(self):
        print("in show method")
    
class Traingle(Shape):
    def area(self,breadth,height):
        result=0.5*breadth*height
        return result
    
    
T=Traingle()
r=T.area(10,10)
print(r)