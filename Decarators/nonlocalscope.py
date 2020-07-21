y=10 # global variable

def outer():
    z=15 # Z is enclosed variable 
    global y
    y=y+6 #UnboundLocalError: local variable 'y' referenced before assignment
    print("y in enclosed function",y)
    def inner():
        x=4   # local variable
        global y
        y=y+8 #UnboundLocalError: local variable 'y' referenced before assignment
        print('y in nested function',y)
        nonlocal z  
        z=z+1  # UnboundLocalError: local variable 'z' referenced before assignment
        print("X value is ",x) # 4 
    inner()
    print("Z is ",z)
    
outer()


def show():
    prin("hello")


# 