from functools import reduce

listx=[1,2,3,4,5]
listsum=sum(listx)
print(listsum)

j=0
for i in listx:
    j=j+i
print(j)

#reduce
result=reduce(lambda x,y: x+y,listx)
print(result)


map --apply on each element 
filter -condition 
reduce - sum, avg, mean, mode, meadian 

first param - function 
second param - sequence 
    