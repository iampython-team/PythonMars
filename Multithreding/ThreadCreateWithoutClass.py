from threading import Thread

def displaySeq(name):
    for i in range(10):
        print("Thread Value is ",i,name)
        
        
t1=Thread(target=displaySeq("python")) # creation of thread with out user defined class 
t1.start()


t2=Thread(target=displaySeq("go")) # creation of thread with out user defined class 
t2.start()
        
        