
listx=[1,2,3,4,5] # __init__ 
print(listx) #private heap space 
print(type(listx))
print(type(print()))
x=2 # __init__
del listx,x # __del__(self)
print(listx) # stack 
print(x)