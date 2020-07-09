
try:
    a=2
    print(a) # name error 
    
    x=5
    result=x/0 # zero division error 
    
except NameError as e:
     print('Exception is raised',e)
     