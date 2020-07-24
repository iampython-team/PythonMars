# OverLoading - Constructor, Method and Operator 

# Constructor Overloading is not supported in the python 

# Method Overloading is not supported in the python

# Overwrite 
class A:
    def __init__(self):
        pass
    
    def __init__(self,param1):
        pass
    
    def add(self,x,y): 
        pass
    
    def add(self,x,y,z): # 4 
        pass
    
    
rohail=A(4)
rohail.add(8,9,0,1) # self+4=5 
    
    
    