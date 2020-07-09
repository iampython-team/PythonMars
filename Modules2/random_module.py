import random

# 0.0 to 1.0

print(random.random())
#0.2461470773106179

print(random.randint(350,760))

listx=[3,"one","two"]
set_test={9,0,0,0,12,14}
print(random.choice(listx))
#print(random.choice(set_test))


print(random.choices(listx,cum_weights=[8,1,9],k=10))


# random index positions - two -1 one -1 10

numbers=[2,4,6,8,10,12,14]
random.shuffle(numbers)
print(numbers)


for i in range(5,25): 
    random.seed(4) 
    print(i)
    print(random.randint(1,10))  # 1-10
    print(random.random())  # 0 -1 