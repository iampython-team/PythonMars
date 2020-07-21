
def month_Name_Decarator(expr):
       def upper_d(func):
           def inner():
                return func() + expr.upper()
           return inner
       return upper_d
       

@month_Name_Decarator("July")
def month():
    return "This month is "

print(month())





