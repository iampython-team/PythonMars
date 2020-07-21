
def addtwonumbers(a,b):
    #print(a+b)
    return a+b    
add2=addtwonumbers(5,6)
add2
print("*******************")
print(add2) # 11
print(add2)
print("*******************")

def f():
    print('hello - world')

print(f) # address

g=f  # g - reference variable to f 
print(g) # address of f
g() # hello
print("======")
g
print("======")
j=g # j - reference to f 
print(j) # address of f 
j() # hello




# functioname - address 
# functionname() - o/p of the function 
# funcationA=functionB functionA is reference functionB


def sumvalues(x,y):
      print(x+y)
      
s1=sumvalues(5,6) # 11 s1=11
print("=======")


locals 
globals
---------------
global
nonlocal

