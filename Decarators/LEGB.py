
#B
x=19 # global -G
y=x
def outer():
    #x=3 # enclosed -E
    def inner():
        #x=6
        print(__name__) # local -L
    inner()
        
outer()

print(x,y)