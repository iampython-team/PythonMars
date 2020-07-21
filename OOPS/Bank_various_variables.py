
# instance variable / object / instance methods and cons 
# static variable / class  / outside of instance methods and cons 
# local variable / normal method 

class Customer(object):
    # class variable 
    bannkname='DBS Bank' # static variable / class variable
    
    def __init__(self,customername,accoutnumber):
        noofloans=4  # local variable 
        self.customername=customername # instance variable
        self.accoutnumber=accoutnumber
        
    def displayCustomerInfo(self):
        noofloans=2 # local variable
        print("****Customer Details***")
        print("========================")
        print("Custome Name",self.customername)
        print("Custome Accoutnumber",self.accoutnumber)
        #print(Customer.bankaccounttype)
        print(Customer.bannkname)




c1=Customer('John','AC123445')
c1.displayCustomerInfo()
# print(c1.bannkname)
# print(Customer.bannkname)

# we can declare the instance variable outside of the class by using object reference 
c1.customeloanamount=10
print(c1.customeloanamount)

Customer.bankaccounttype='Savings'
print(Customer.bankaccounttype)