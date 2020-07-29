
# constructor data 
# instance method data 

class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # 100 
        
    def display(self):
        print('name of employee',self.name)
        print('age of employee',self.age)
        
        
class HR(Employee):
    def __init__(self,name,age,recruterid,talenteamcategory):
        # self.name=name
        # self.age=age
        # 100 
        super().__init__(name,age)
        self.recruterid=recruterid
        self.talenteamcategory=talenteamcategory
        
        
    def display(self):
        super().display()
        print('Recuriter id is ',self.recruterid)
        print('HR Catgeory id is ',self.talenteamcategory)
       
        
class SoftwareEngineer(Employee):
    def __init__(self,name,age,projectname,technology):
        # self.name=name
        # self.age=age
        # 100 
        super().__init__(name,age)
        self.projectname=projectname
        self.technology=technology
      
        
        
        
        
h=HR('John',25,1001,'globalteam')
s=SoftwareEngineer('Donalnd',28,'COBRA','AI')
h.display()
s.display()
    