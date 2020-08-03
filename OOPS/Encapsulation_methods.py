
class Student:
    
    def marks(self):  # instance method 
        tm=89
        self.__x=5
        return f'student marks : {tm}'
    
    def __specialExam(self): # private instance method
         return "this is special marks : 98"
     
     
s=Student()
print(s.marks())
#print(s.__specialExam())
print(s._Student__specialExam()) # Mangling - _class name 
print(s._Student__x)
     
     

     
     