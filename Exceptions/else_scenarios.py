# else - after if 
# else - after loops (while,for)
# else - except 

a=2 
if a>=5:
    print(a)
else: 
    print('else')
    
    

for  x in range(10):
    if x >=5:
       break
    print('x is ',x)
else:
    print('all statements are executed ')
    if True:
       a=4
       print('hello',a)
      
print("done")

try:
    print('try',2/0)
except: 
    print('exception')
else:
    print('else')
    
    
# if true - no else 
# break in for/while - no else 
# exception is thrown - no else