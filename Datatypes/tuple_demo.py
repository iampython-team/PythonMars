
# dynamic data - list
# static data - tuple


system_data=()
print(type(system_data))
numbers="raja",
print(type(numbers))
x,y,z=1,2,3

g=['English','Spanish']

person=('name','age','gender',('locations',),45,78.9,g)
print(person)


#list - all datatypes
print(person[3:5])
print(person[-1])
t1=(1,2,3,3)
t2=(4,5,6,5)
print(t1+t2)

#TypeError: 'tuple' object does not support item assignment
tex=(1,2,3,3)
#tex[3]=4
#print(tex.index(3,0,1))

print(tex.count(3))


