class Duck :
    def quack(self,name):
        print("Quacked")
        
class MallarDuck:
    def quack(self,name):
        print('louder quacked')
        
        
class Eagle:
    def fly(self):
        print("i just fily")
        
        
class MakeitQuack:
    
    def __init__(self,bird):      
        bird.quack('forest')
        #bird.fly()
        
        
MakeitQuack(Duck())
MakeitQuack(MallarDuck())
#MakeitQuack(Eagle())
        
        
        
    

    
        
    
    
    