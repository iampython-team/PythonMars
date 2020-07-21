# fnmf nnf nfn nm

# in module -function - def functionname()
# in class - method ( access by method), __init__ constructor 

# def __init__(self):
#     pass
class Student(object): # class Student:  class Student()
    ''' this class describes about the student '''
    
    # Constructor 
    def __init__(self,studentid):
        self.sid=studentid  # studentid is normal variable, 
                            # self.sid is instance variable
        print("Student id -",self.sid)
        
        
    # Instance method 1
    def getStudentInfo(self,sname,sage):
        self.sname=sname
        self.sage=sage
        print("self sid in instace method 1",self.sid)
        print("Student name ",self.sname)
        print("Student age",self.sage)
       # print('student marks',self.year1)
        
    # instance method 2 
    def studentMarks(self,year1):
        #self.year1=year1
        print("self sid in instace method 2",self.sname)
        print("year1 marks",year1)
        
        
 
        
s1=Student(1001) # creation of an object, s1 is object reference 
s2=Student(1002) 

s1.getStudentInfo('John',17)
s2.getStudentInfo('Obama',14)


s1.studentMarks(78.98)
s2.studentMarks(85)



        
        
        
        
        
        
        