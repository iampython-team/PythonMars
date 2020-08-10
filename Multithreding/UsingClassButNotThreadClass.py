from threading import Thread

class MyThread:
    def printtoptenvalues(self):
        for i in range(10):
            print('class thread -',i)
            
            
task= MyThread()      
t=Thread(target=task.printtoptenvalues) 
t.start()  
