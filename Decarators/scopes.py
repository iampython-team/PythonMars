

a=2  # global 
b=5   # global
def outer():  # enclosed function 
    global b
    b=b+6 #UnboundLocalError: local variable 'b' referenced before assignment
    b=6 # enclosed variable 
    print(b)  # b=6 
    def inner():  # nested function or inner function
        c=5 # local variable 
        print(a) #  2
        print(b) # 6
    inner()
        
outer()
print(a,b)


# global variables cannot be modified with in functions without global keyword

        