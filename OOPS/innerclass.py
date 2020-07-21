class Outer():
    y=10 # class name 
    def __init__(self):
        print("outer class constructor")
        
        
    class Inner():
        x=5 # class name 
        def __init__(self):
            print("Inner class constructor")
            
        def show1(self):
            print("In Inner class -Show method 1")
            
        def show2(self):
            print("In Inner class -Show method 2")
            
            
# Approach 1
outer_ref=Outer()
outer_ref.Inner().show1()
print(outer_ref.Inner.x)
print(Outer.Inner.x)
#inner_ref=Inner()
print("===============")
# Approach 2 
outer_ref1=Outer()
iref=outer_ref1.Inner()
iref.show1()
iref.show2()
print(iref.x)
print(Outer.Inner.x) # X is class variable 
print("===============")
Outer().Inner().show1() # instance method 



# class - class static variable 
# object - constructor - instance data 



