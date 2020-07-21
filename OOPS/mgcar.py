class Car:
    carname = "MG"  #class variable

    def __init__(self,model,year,*available,**branchhead):
        Car.companyCEO ='William'  #class variable
        self.model= model
        self.year = year
        self.available =  available
        self.branchhead = branchhead
    
    def showCarDetails(self):
        Car.headquarters = 'London'  #class variable
        print("Company Carname", Car.carname)
        print("Company CEO is ", Car.companyCEO)
            
    @classmethod    
    def carFounders(cls):
        cls.founderName = 'Donald'
        print(cls.founderName)
        
    @staticmethod
    def getProduced2019(count):
        Car.parentcompany = 'XYZ'
        print(count)
        print(Car.parentcompany)
        
car1=Car('hector', 2019, 'India', 'UK', 'Poland', uk_branch='Roy', india_branch='Joy')
car1.showCarDetails()
    
Car.carFounders()
Car.getProduced2019(1000)

car1.getProduced2019(2000)

