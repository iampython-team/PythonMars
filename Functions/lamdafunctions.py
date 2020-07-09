#Anonymous or lamda

lambda parameter_list: expression

addingtwo=lambda x:x+2
print(addingtwo(5))

addxy=lambda x,y: x+y
print(addxy(1,2))


def addingTwoVar(x,y):
    result=x+y
    print(result)
    
addingTwoVar(1+2,4+5)

# areaofcube=lambda X,Y,Z,*K: X*Y*Z*tuple(K.values())
# print(areaofcube(1,2,3,a=2,b=5))

x=3
a=2
y=(6,7)
print(a*x*y)

t=2
d={'a':2,'b':5}
l=[3,4,5]
print(t*l)


u=2
v=2
x=(3,4)

print(u*v*x)



