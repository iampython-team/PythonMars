
s='5.5+7.5'
listex=s.split('+')
print(listex)
for i in listex:
   x=float(i)
   print(x)
   
import itertools

for numbers in itertools.combinations(listex,2):
    if sum(numbers) == target:
        print([integer_array.index(number) for number in numbers])