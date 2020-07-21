import gc 
import time 
class TestGargabageC(object):
    def __init__(self):
        print("object is created")
        
    def __del__(self):
        print("objection deletion .....")
        
        
        
print(gc.isenabled()) # True 
y=5
print(y) # 5 
gc.disable()
print(gc.isenabled()) 
object_ref=TestGargabageC() # object is created
x=2 
print(object_ref)
del object_ref

print(x) # 2 

#print(object_ref)

#time.sleep(10)
print("application closed")
        
        
