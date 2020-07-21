
# Print First N numbers 

def firstnum(number):
    n=5
    while n<= number: 
        yield n
        n=n+1
        
       # n+=1f

for x in firstnum(15):
    print(x)
    

# generators are iterators 
