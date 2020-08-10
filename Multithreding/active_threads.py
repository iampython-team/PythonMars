from threading import Thread, active_count, current_thread
import time



def displayThread():
    print(current_thread().name,"-------- Started")
    time.sleep(1.5)
    print(current_thread().name,"-------- ended")
    
    
    
print("Number of active threads - before thread call",active_count())
t1=Thread(target=displayThread,name='Raja')  # thread is created / not in active / start 
t2=Thread(target=displayThread,name='hello')
t3=Thread(target=displayThread,name='Thread3')
t4=Thread(target=displayThread,name='Thread4')
print("Number of active threads - before thread start method",active_count())
t1.start()
t2.start()
t3.start()
t4.start()
print("Number of active threads - after thread call",active_count())
time.sleep(10)
print("Number of active threads - final call",active_count())


    