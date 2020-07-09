

listx=[1,2,3,4,5] # object 1

newlist=[] # object 2 
for i in listx:
    i=i**2
    newlist.append(i)
print(newlist)

#map(function, sequence )

def sqaureValues(n):
     return n**2
output=map(sqaureValues,listx)
print(list(output))


# map(lamdafunction,sequnce)
output3=map(lambda n: n**2, listx)
print(list(output3))

print(list(map(lambda n: n**2, listx)))


numbers=[1,2,3,4,5,6,7,8,9,10]

newlist=[]
for i in numbers:
    if i%2 == 0:
        newlist.append(i)
print(newlist)
        
def even_Numbers(n):
     if n%2==0:
         return n
 
print(list(map(even_Numbers,numbers)))
# task , inputs 
1 2 3 4 5 6 7 8 9 10 
None 2 3 

print(list(filter(lambda n: n%2 ==0, numbers)))
 



