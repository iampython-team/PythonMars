
# closure 
def outer():
    x=3 
    def inner():
        return x+8  
    print("this is inner",inner)
    return inner()
    
objinstance=outer()
print("this is inner but calling outside of the function",objinstance)




# outer ---> outer() 
# inner ---> inner() -- 


# function can be assigned to function or any object

