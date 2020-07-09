
number1=int(input('Enter the number 1 :'))
number2=int(input('Enter the number 2 :'))

#arthmatic= number1/number2
#print(arthmatic) #ZeroDivisionError: division by zero

try:
    arthmatic= number1/number2
    print(arthmatic)
except:
     print('Exception is raised - Please enter the proper input')




