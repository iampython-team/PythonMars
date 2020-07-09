
numbers=(1,3,3,4,5,6,7,8,9)
# add 5 to every item in the tuple 
def add5(n):
    n=n+5
    return n
    
add5map=list(map(add5,numbers))
print(add5map)
print(tuple(add5map))
print(set(add5map))



team_members =['Raja','mahendra','john']

def teamupper(str):
        str=str.title()
        return str
    
teamupperdata=list(map(teamupper,team_members))
print(teamupperdata)


l=list(map(lambda str: str.upper(),team_members))
print(l)


numbers=[1,2,3,4,5,6,7,8,9,10]
# evenumbers - sqaure 
def evennumbers(n):
     if n%2==0: 
         return n**2
      
    
# true, false  

#  nested lamdas 
evenfilter=list(filter(evennumbers,numbers))
print(evenfilter)

def sqaurefunction(n):
     return n**2
    

finaldata=list(map(evennumbers,evenfilter))
print(finaldata)


# map reduce filter 
# operation  expression true/false
