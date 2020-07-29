
class A:
    
    def a(self):
        print("aaaa") 
        
        
class E():
    def e(self):
        print('eeee')


class B(A):
    def b(self):
        print('bbbb') 

class C(E):
    def c(self):
        print("cccc") 

class D(C):
    def d(self):
        print("dddd")


d_obj=D()
d_obj.a()

