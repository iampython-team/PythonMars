

class Parent():
    a=10
    def __init__(self):
        self.b=100

class Child(Parent):
    def show(self):
        print(super().a)
        print(self.b)
        
cobj=Child()
cobj.show()
