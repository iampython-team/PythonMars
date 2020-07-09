greeting="hello,good,morning!,morning morning"

print(greeting.upper())
print(greeting.lower())
print(greeting.title())
print(greeting.index('morning')) #wrong inpiut - error  to find the index
print(greeting.count('morning')) # count is o if it not found 
print(greeting.casefold()) # if else
print(greeting.find('good')) # -1   ---> to find the index
print(greeting.center(105,'/'))

#short string
name='hi'
print(name.center(7,'*'))

print(greeting.replace('morning','evening',-1))

print(greeting.split(',')) # always returns list

print(greeting.startswith('ello'))
print(greeting.swapcase())

# what is diff b/n casefold and swapcase 

#print(greeting.translate('H'))



# immutable 
# some string operations 
# control structures


