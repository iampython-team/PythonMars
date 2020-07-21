
import time 
import random
regions=['ASIA','EUROPE','NORTHAMERICA','AFRICA']
countries=['Singapore','Norway','USA','SouthAfrica']

def people_list(num):
    results=[]
    for i in range(num):
        person={
            'id':i,
            'region':random.choice(regions),
            'country':random.choice(countries),
        }
        results.append(person)
    return results

def people_generator(num):
    for i in range(num):
        person={
            'id':i,
            'region':random.choice(regions),
            'country':random.choice(countries),
        }
        yield person
    return None

# print(people_list(10))
# print("==================")
# for i in people_generator(10):
#     print(i)

t1=time.perf_counter()  # clock  current 
#people=people_list(100000) 
for p in people_list(10):
    print(p)
t2=time.perf_counter()  # clock 
print('Time taken for List',t2-t1)

t3=time.perf_counter()
#people_generator(100000)
for p in people_generator(10):
    print(p)
t4=time.perf_counter()
print('Time taken for Generator',t3-t4)
print(dir())

# gen - iter - all values 
# memory - next() - one item  
# perfomanance 



# memory 
# perfomance 

# dundle /magic 

# __iter__, __next__


