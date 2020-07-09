
x={'One':(1,2,3)}
print(x)

keys=('A','B','C','D')
key=1
strings="hello"
v=567
y={}
y=y.fromkeys(strings,v)
z=dict.fromkeys(keys,v)
print(y)
print(z)


person={
    'name':'John',
    'age':45,
}

person.setdefault('city','NY')
print(person)


person.setdefault('name','Robert')
print(person)

person['language']='French'
print(person)

