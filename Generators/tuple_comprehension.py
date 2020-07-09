tupleValues=(x for x in range (4))
rangenumber=tupleValues # generator
try:
    print(next(rangenumber))
    print(next(rangenumber))
    print(next(rangenumber))
    print(next(rangenumber))
    print(next(rangenumber))
except StopIteration as e:
    print("No element found in the generator",e)
    

def getValues(number):
    # this is empty - generator or  iterator
    for i in range(number):
        print(i)
        yield
        
next(getValues(9)) 
next(getValues(100))

