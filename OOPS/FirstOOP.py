def person():
    print("hello")
    
    
    
class Person: # class name should starts with uppercase 
    
    ''' This class is defined for Person info '''
    
    name='Raja'
    age=45
    country='India'
    
    def speak(self):
        print("English")
        
    def write(self):
        print("he writes in English")
           
objref=Person()  # create an object and assigned reference variable
 
objref.write()  # accessing the instance methods by using object refer
objref.speak()

print(objref.name) # accessing the variables by using the object reference
print(objref.age)
print(objref.country)

print(Person.__doc__)