from threading import Thread
import time


def task1(numbers):
    for i in numbers:
        time.sleep(1)
        print("Double of numbers ---",i*2)
        
def task2(numbers):
    for i in numbers:
        time.sleep(1)
        print("Square of numbers ---",i**2)
        
numbers=[1,2,3,4,45,5,56,6]

starttime=time.perf_counter()
t1=Thread(target=task1,args=(numbers,),name="thread--1")
t2=Thread(target=task2,args=(numbers,),name="thread--2")
t1.start()
print("===")
t2.start()

t1.join()
t2.join()

endtime=time.perf_counter()

totaltime=endtime-starttime
print("time taken for processing threads",totaltime)