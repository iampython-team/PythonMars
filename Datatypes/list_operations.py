numbers=[1,2,3,4,5]
extranumbers=[6,7,8]
s='dhoni'


# insertion opertions 
    # insert(), append(), extend() 
# deletion operations 
   # remove(), pop(), clear()
# other operations
  # count, index, ..... 
  
numbers.insert(2,'raja')
print(numbers)

numbers.append(12)
print(numbers)
sports=['cricket','baseball']
numbers.append(sports)  # insert the item at the last
print(numbers)

numbers.extend('raja')
print(numbers)

# deletion 
primenumbers=[2,3,5,5,5,7,11]
print(primenumbers)
primenumbers.pop(3) # delete last item from list, 3 index
print(primenumbers)

# 

primenumbers.remove(5) # 5 is an item
print(primenumbers)

primenumbers.clear()
print(primenumbers)


listx=[1,2,3,4] # memory address 7890123
listy=listx.copy() # listx listy 
print(listy)


listz=listx # memomry address 7890456
print(listz)


num=[9,7,6,3,1,9,9]
print(num.count(9))

print(num.index(9,5,9))

# 9 - element - (list)
# 1 - start eindex or 6 end index

snames=['Tennis','Baseball','Cricket','Volleyball']
sscore=[198,34,67,12,989]
snames.sort()
sscore.sort()
print(snames)
print(sscore)

#TypeError: '<' not supported between instances of 'str' and 'int'
#stringvalues=[1,"one",2,3,4,'Two','Four',4.56]
#stringvalues.sort()
#print(stringvalues)

sscore.reverse()
print(sscore)

sscore.sort(reverse=True)
print(sscore)




