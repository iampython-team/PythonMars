
#arg 1 must be a string, bytes or code object
age=45
print(eval('age+15'))

b=bytes(51) # int - bytes
d=bytes('hi',encoding='utf-8') # str, encoding
print(b)
print(d)

#print(eval(b))
x=2 
y=bytes(2)
#z=int(y)

#print(x,y,z)
listx=[1,2,3]
print(eval('listx'))

name='2+1'
e=eval(name)
print(e)




#print(sqrt(9))
# 8/2 = 0, 16 
print(pow(2,4,5))
# power value 
# powervalues/thirdpoistionvalue = r


print(divmod(4,3)) # 4/3 - q,r
#4/3 - 1 1 

from math import * 
cal= {'+':sqrt,'-':pow}
eval('dir()',cal)
print(dir())
print(eval('1(9)',cal))


import math 
print(math.sqrt(8))
print(math.sin(90))