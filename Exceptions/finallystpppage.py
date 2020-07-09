import os

try: 
    print('this is finally block stoppage')
    os._exit(0) # python intrepter
    print('after the calling OS module exit ')
except:
    print('except')
finally: 
    print('finally block')
    
print('hello ..... ')
    
