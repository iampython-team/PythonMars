def wish_upper(wish): # actual function as input to decarator function 
    def task1():
        wishstring=wish()
        return wishstring.upper() ## implementing the closure
    return task1 # implementing the closure

def wish_title(wish): # actual function as input to decarator function 
    def task2():
        wishstring=wish()
        return wishstring.title() ## implementing the closure
    return task2 # implementing the closure


def wish_split(wish): # actual function as input to decarator function 
    def task3():
        wishstring=wish()
        return wishstring.split('') ## implementing the closure
    return task3 # implementing the closure

@wish_title # second call
#@wish_split # first call 
@wish_upper
def wish():
    return "good morning! Python Developer!"

print(wish())
#taskobj=wish_upper(wish)
#print(taskobj())



