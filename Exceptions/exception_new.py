
try:
    print(4/0)
    
except BaseException as msg: # PVM - create an object for every exception 
       print(msg)
       print(type(msg))
       print(msg.__class__)
       print(msg.__class__.__name__)
finally:
    print('always executes')