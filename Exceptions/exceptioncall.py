try: 
    x=int(input('Enter the first number :'))
    y=int(input('Enter the second number :'))
    print('the result : ',x/y)
    
except Exception as z:
    print('please provide input',z) 
    
    
except ZeroDivisionError as z:
    print('Cannot divide with zero',z)
    