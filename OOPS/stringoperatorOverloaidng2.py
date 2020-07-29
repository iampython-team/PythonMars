class Customer():
    def __init__(self,cname):
        self.customername=cname
        
        
    def __str__(self):
        return "raja"
        
        
    def __add__(self,other):
         totalcoustomer=self.customername+other.customername
         customerfinaldata=Customer(totalcoustomer)
         return customerfinaldata
        
        
c1=Customer('Sachin')
c2=Customer('Ramesh')
c3=Customer('Tendulkar')
c4=Customer('Rahul')
print(c1+c2+c3+c4)


h="hello"
print(str(h))

print(repr(h))


import datetime
today=datetime.datetime.now()
#print(today)


print(str(today))
print(repr(today))
    