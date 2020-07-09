
name="baseball"
print("my fav sport is %s." %name)

person_name='John'
person_age=45
print("Person details, person name is %s and person age is %s" %(person_name,person_age))

rice=4.53
milk=2.67
print('rice quantity %f and milk quantity %0.1f' %(rice,milk))
# %s, %d, %i, %f, %x ... 


# format 
# %s,%d 
# f-strings  3.6 498 PEP
sportname='baseball'
score=78.9
print(f'i like {sportname}')
print(f"my score is  {score}")


# expressions 
print(f'{True == False}')

#functions 
def to_uppercase(string):
    return string.upper()

greetings='hello, good morning'

print(f'{to_uppercase(greetings)} --- ciao / Italian greeting')

# multiple f-strings
name="raja"
messages=(
    f'hi {name}',
    f'hello {name}',
    f'hey {name} ',
)
print(messages)

rice=4.53
milk=2.67
#print(f'rice is  {rice}')
