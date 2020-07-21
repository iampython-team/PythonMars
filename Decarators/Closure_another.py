
def arithmaticop():
    a=4 
    def addTwoNumbers():
        b=5
        result=a+b
        return result
    return addTwoNumbers()

print(arithmaticop())  # enclosed function call #<function arithmaticop.<locals>.addTwoNumbers at 0x7fe305aee700>
add2=arithmaticop()   # 
print(add2)  # addTwoNumbers

def name():
    print("hello")
    
print(name)

# function name -----> addresss
# functionanme() - function call 