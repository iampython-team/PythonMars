from threading import Thread

class MyThread(Thread):
    def run(self):
        for i in range(10):
            print('class thread -',i)
            
            
t1=MyThread() 
t1.start()

            
t2=MyThread()
t2.start()


    