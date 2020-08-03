from abc import ABC,abstractmethod

class Parent(ABC):
    g=157
    
    @abstractmethod
    def method1(self):
        pass
    
    def method2(self):
        print("parent abstract class - method2")
        
        
class Child(Parent):
    def method2(self):
        super().method2()
        print(Parent.g)
        print(super().g)
        print("child implementation class")
        
        
c=Child()
c.method1()