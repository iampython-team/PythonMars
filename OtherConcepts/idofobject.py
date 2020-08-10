
a=2 

x=5 

print(id(a))

a=2
a+=3
a=5
print(id(a))

a=5
b=10
c=a+b
print(id(a))
print(id(b))
print(id(c))


print("==========")

p=5
q=p
print(id(p))
print(id(q))


name1="raja" 
name2="raja"
print(id(name1))
print(id(name2))

print(name1==name2)

print(name1 is name2)

list1=[]
list2=[]
print(id(list1))
print(id(list2))
print(list1==list2)
print(list1 is list2)

tuple1=()
tuple2=()
print(id(tuple1))
print(id(tuple2))
print(tuple1 == tuple2)
print(tuple1 is tuple2)


# == - compares value 
# is - compare id 
