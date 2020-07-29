

# isinstance - True when 

class A :
    pass 


class B(A):
    pass 



a=A()
b=B()
print(isinstance(a,B))


print(issubclass(B,A))  # child, parent 
print(issubclass(A,B))  # parent child

print(issubclass(int,bool))
print(issubclass(bool,float))