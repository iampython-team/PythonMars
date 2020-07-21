
a=2 
b=3 
print(globals())
print(locals())
if globals() is locals():
    print('both are equal')

def someData():
    name='raja'
    print('name',name)
    print('locals',locals()['name'])
    #print('name',globals()['name'])
    if globals() is not locals():
        print('both are  not equal')
    
someData()
if globals() is locals():
    print('both are equal')