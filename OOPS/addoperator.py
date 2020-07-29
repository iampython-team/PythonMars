class ac: 
    def __init__(self,a): 
        self.a = a 

    def __add__(self,p): 
        k = self.a+p.a 
        return ac(k) 

x=ac(7) 
y=ac(5) 
z=ac(10) 
r=ac(10)
res=x+y+z+r
print(res.a)


