import time

# listx =[1,2,3,4,4,5,5,5,,5]
def countDown(number):
    print('count')
    while number > 0:
        yield number
        number=number-1
        
countvalue=countDown(1)
for x in countvalue:
    print(x)
    time.sleep(2)

