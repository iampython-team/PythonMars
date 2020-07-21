
# input string = 'november'
# ouput value - list - ['n','0','v'------]

outputlist=[]
inputstring='november'
for letter in inputstring:
    outputlist.append(letter)
    
print(outputlist)

outputlist2=[ letter for letter in inputstring ]
print(outputlist2)


#[ [var1,var2....var3] for item in sequenceobject ]


# range(1,100)  even numbers - list 
# variable declaration before for loop in list comprehesion. 
# conditions after the for loop
even=[ [x1,x2] for x1 in range(15) if x1%2 == 0
      for x2 in range(10) if x2%2 == 0]
print(even)


# if else before for loop in list comprehesion
newstyle= [ "even" if i%2== 0 else "odd"  for i in range(10)]
print(newstyle)
