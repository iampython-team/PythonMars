from abc import ABC,abstractmethod
class Animal(ABC):
      @abstractmethod
      def move(self):
            pass 
        
class Snake(Animal):
    def move(self):
        print("i can crawl")
        
class Dog(Animal):
    def move(self):
        print("I can run")
        
class Tiger(Animal):
    def move(self):
        print("i can roar")
        
        
#a=Animal()
tobj=Tiger()
tobj.move()


dobj=Dog()
dobj.move()


print(issubclass(Dog,Animal))
print(isinstance(tobj,Dog))