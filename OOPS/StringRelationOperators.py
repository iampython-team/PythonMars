
class StringOperators():
    
    def __init__(self,name):
        self.name=name
        print(self.name)
    

sobj1=StringOperators("hello")
sobj2=StringOperators("hello")
print(sobj1.name==sobj2.name)
print(id(sobj1))
print(sobj1)
print(id(sobj2))
print(sobj2)


empname1="john"
empname2="john"

if empname1 == empname2:
    print("matched")