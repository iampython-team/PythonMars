

d={ num:num*56 for num in range(5)}
print(d)
print(type(d))

person={
    'name':'John',
    'age':45,
    'location':'NY'
}

d2={ k.upper():v for k in person.keys() for v in person.values() }
print(d2)