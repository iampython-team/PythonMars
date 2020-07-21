def raja(func):
    def inner(*args):
        #   if y ==0: 
        #       return "y value should not be zero"
        #   elif z==0:
        #       return "z value should not be zero"
        #   else:
        #       return x/y/z     
        list1=[]
        list1=args[1:]
        for i in list1:
            if i==0:
                return "give proper input"
        return func(*args)
    return inner # closure
               
@raja
def div1(a,b):
    return a/b

@raja
def div2(a,b,c):
    return a/b/c

print(div1(2,7))
print(div2(4,4,0))

#print(div1(2,4)) # second value should not  be zero
#print(div2(2,5,9)) # second and third value should bot be zero