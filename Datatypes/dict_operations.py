person={
    'id':12345,
    'name':'XYZ',
    'height':6.5,
    'languages':['Spanish',['BEnglish','AEnglish'],'Italian'],
    'addreses':('res','ofc'),
    'M':True,
    'edu':{'UG','PG'},
    0:None,
    'comp':4+5j,
}
print(person['name'])
print(person[0])
print(person['languages'][1][1])

print(person.get('languages')[1][1])

# get() - no error if key is not found - None
# ['key'] - error if key is not found 

print(person.keys())
print(person.values())
print(person.items())

print("===========================")
samplelist=[(1,'One'),(2,'two'),(3,'Three')]
newdict=dict(samplelist)
print(newdict)

sampletuple=([1,'one'],[2,'two'],[3,'Three'])
dicttuple=dict(sampletuple)
print(dicttuple)

dict1={1:'one'}
dict2={3:'three',4:'four'}
#print(dict1+dict2) # collections

dict1.clear()
print(dict1)
dict2.pop(3)
print(dict2)
dict2.popitem()
print(dict2)





