class Parent1: 
    def show(self): 
        print("in parent 1 - show method") 

class Parent2(Parent1): 
    def show(self): 
        print("in parent 2 - show method") 
        #super().show() 

class Parent3(Parent1): 
    def show(self): 
        print("in parent 3 - show method") 
        #super().show() 

class Parent4(Parent1): 
    def show(self): 
        print("in parent 4 - show method") 
        #super().show() 

class Child(Parent2,Parent3,Parent4): 
    def show(self): 
        print("in child - show method") 
        #super().show()
        super(Parent4,self).show()
        
print(Child.mro()) # child,parent2, parent3, parent4, parent1, object 
                  # child,parent2,parent3,parent4,parent1,object 
#child,parent2,parent1,parent3,parent4,object
# child, parent2,parent3,parent4,parent1,object
# child,paent2
c=Child()
c.show()