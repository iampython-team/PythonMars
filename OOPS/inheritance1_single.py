
class Parent(object):
    def __init__(self) : 
        print('parent constructor call') 
        
    def parentMethod(self):
        print("parent method")


class Child(Parent):
        def __init__(self) : 
           print('child constructor call')  
           
        def childMethod(self):
            print("child method")
            
                      
# parent_obj=Parent()
# parent_obj.parentMethod()

child_obj=Child()
child_obj.childMethod()
child_obj.parentMethod()


