

# set1 set2 --> union, | 
# set1, stet2 ---> intersection, & 
# set1, set2 --> difference, -

set1={1,4,5,7}
set2={5,6}
print(set1.union(set2))
print(set1 | set2)

print(set1.intersection(set2))
print(set1 & set2 )


print(set1.difference(set2))
print(set2.difference(set1))
print(set1 - set2)
print(set2 - set1)

set1.intersection_update(set2)
print(set1)

set2.intersection_update(set1)
print(set2)

set1.difference_update(set2)
print(set1)

set2.difference_update(set1)
print(set2)


set3={4,5,6,7}  
set4={1,7,8,6}

print(set3.symmetric_difference(set4))
print(set3 ^ set4)

''' 
s1 - S2 = remove intersection value = s1 1,2,3  =1,2 
                                      s2 3,4,5
s2- s1                                           4,5 
                                      
                                      
                                      
s1 ^ s2 = remove intersection values= s1 1,2,3  1,2,4,5
                                      s2 3,4,5  
                                      
s2 ^ s1                              1,2,4,5

 '''
 

oldset={1,4,5,6}
oldset.add(False)
print(oldset)


newset=oldset.copy()
print(newset)

newset.discard(15)
print(newset)

newset.pop()
print(newset)
newset.pop()
print(newset)

x={1,3,7,8}

x.update([1,2,3])
print(x)


primenumbers={2,3,5,7} # set 
print(frozenset(primenumbers))
fz=frozenset(primenumbers)
print(type(fz))


