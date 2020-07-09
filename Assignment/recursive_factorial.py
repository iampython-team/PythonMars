def factorial(num):
    if num==1:
        return 1
    else:
        fact=num*factorial(num-1)
        return fact
    
print('The factorial of number',factorial(5))



