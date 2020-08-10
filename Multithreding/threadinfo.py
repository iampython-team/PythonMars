from threading import Thread,ThreadError

def job():
    print("job execution----")
    
try:    
    t1=Thread(target=job)
    t2=Thread(target=job)
except ThreadError as thredexcep:
    print(thredexcep)


print(t1.isDaemon())
t1.setDaemon(True)
print(t1.isDaemon())

 
print(t1.getName())
print(t2.getName())
t1.start()
print(t1.is_alive()) # working method
#print(t1.isAlive()) # deprected

t1.setName("hello")
 
print(t1.getName())




