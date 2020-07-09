# in  - lookup

# for iterationvariable in Seqence/map:
# print(iterationvariable)

employee=['A',1,True,'Hello'] # 0123 
print(employee)
# don't singe letter
for emp in employee:
      print(emp)
      
tuplex=(2,3,4)
for tup in tuplex:
    print(tup+2)
    
setx={1,4,5,5,5,5,5,5,9}
for iter in setx:
    print(iter)
    
person={
    'name':'John',
    'age':45,
    'city':'NY'
}

print(person)

for dictvar in person.items():
     print(dictvar)
     
for values in person.values():
     print(values)
     
for key in person.keys():
     print(key)
     
for k,v in person.items():
    print(k,'.....',v)
    
for num in (5,):
    print(num)
# 10 -- prime numbers - 100 
# even numbers 50 
# odd numbers 25
for num in range(1,10):
    if num % 2 == 0: 
        num=num+50
        print(num)

x=set()
print(type(x))
print(x)
 