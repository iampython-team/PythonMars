
x=-45
print(abs(x))

listx=[0]
print(all(listx))

#all -> 0, False,None    -----> False
# empty - True

print(any(listx))
# any -> empty - False
# None -False

t='a'
print(ascii(t))
# a 97 A=65

b=5
print(bin(b))
# 0b ... 


codes='x=2'

# code A file 
# B file --- compile and exec  # modules and files
setx={1,2,3,4,5,10.4,1}
print(sum(setx))

print(dir())



colors=('red','green','yellow','white')
e=list(enumerate(colors,start=78))
print(e)
print(dict(e))

for index,itemname in enumerate(colors,start=67):
    print(index,itemname)
    