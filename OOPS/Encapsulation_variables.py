class Person:
    x=10 # class variable
    __y=5 # private class variable
    def __init__(self):
        self.name="donald"  # instance variable 
        self.__lastname="Trump"  # private instance variable
        
        
    def printName(self):
         print(Person.x)
         print(Person.__y)
         return self.name+'  '+self.__lastname
    
    
p=Person()

print(p.name)
#print(p.__lastname)
print(p.printName())
print(Person.x)
#print(Person.__y)


# Encapsulation -- data --- variable- instance & class , method 