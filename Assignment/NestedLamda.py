

result3=lambda a=5,b=5: lambda *x: a+b+sum(x)
#print("result 3",result3(2,3))

r=result3() # lamda - lamda - memory object location 2 objects 
print(r(4))

def function1(a,*b):
    print(a+sum(b))
    
function1(2,3,4,8,9,1,9,0)


''' x=2
y=(3,4)
z=x+y[0]+y[1]
print(z) '''

# list of numbers, lamda square of even numbers 
numbers=[1,2,3,4,5,6,7,8,9,10]

# filter - even if x %2 == 0 
# map - sqaure of even numbers 
# reduce 
        
        
evennumber=list(filter(lambda x: x%2 ==0, numbers))
sqaureven=list(map(lambda x: x**2, evennumber))
print(sqaureven)

y=lambda x=list(filter(lambda x: x%2 ==0, numbers)): list(map(lambda h: h**2, x))
print(y())








