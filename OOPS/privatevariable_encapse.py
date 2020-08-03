class Parent():
    d=56 # class variable 
    def __init__(self):
        self.__a=5 # private instance variable
        
    def test(self):
        print(self.b)
        
class Child(Parent):
    def __init__(self):
       pass
      
    def method1(self):
        print(Parent.d)
        
        
        
cobj=Child()
cobj.method1()


# private variables cannot be acccessed outside of the class 
# __variablename 
# __methodname 


# dundle methods 
