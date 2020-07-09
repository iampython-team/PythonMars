x='hello'
listx=[12,78,255]
boolx=True
print(bytes(x,encoding='utf-8'))
print(bytes(listx))
print(bytes(boolx))

y=256
print(bytes(y))

# float cannot be converted into bytes 
# bytes range 1-255 
# bytes are immutable

evennumbers=[2,4,6,8,10,12]
print(bytes(evennumbers))
byteevennumbers=bytes(evennumbers)
print(byteevennumbers[0])
print(byteevennumbers[-1])
#byteevennumbers[1]=14 #'bytes' object does not support item assignment

ba=bytearray(byteevennumbers) # bytes to bytearray
print(ba)
print(ba[-1])
ba[1]=14
print(ba)
print(ba[1])

x='3.4' 
print(type(eval(x)))




