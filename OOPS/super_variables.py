

class Parent():
    a=10 # class 
    def __init__(self):
        self.b= 100 # instance
        
    def test(self):
        print(self.b)

class Child():
    def show(self):
       
        print(self.b)
        print(Parent.a)
        print(super().a)
        
cobj=Child()
cobj.show()


# self or instance variable 
# instance method / inheritance 
