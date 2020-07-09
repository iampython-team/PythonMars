#x= eval(input('Enter random x :'))
#print(type(x))
#print(x)


# employee john, 97 projects
name='John'
noofprojects=97
print('Name of the Employee is',name,'No. of projects-',noofprojects)


# format  py3 
# f-string py3.6
# %d, %s, %i, %f py2 

message='Name of the Employee is'+name+'No. of projects-',noofprojects
message2="Name of the 'Employee' is '{0}' No. of projects {1} ".format(name,noofprojects)
print(message2.title())

# s- strings d-decimal base 10 , f-float ,c ,b o x X e 

examavgscore=78.7890
avgscore='Exam averag score {0} ... {1:0.2f}'.format(examavgscore,examavgscore)
print(avgscore)

# int - d 
# float - f 
# s 
numx=[9.5,6.789,0.345]
for i in numx:
    i
    strlist='list formatting {0}.... {1:.2f}'.format(numx,i)
    print(strlist)
strlist='list formatting {0}.... {1}'.format(numx,i)
print(strlist) # TypeError: unsupported format string passed to list.__format__



#map reduce filter - lamda 
name = "Eric"

print("Hello, %s." % name)
name = "Eric"
age = 74
print("Hello, %s. You are %s." % (name, age))

#f-Strings: A New and Improved Way to Format Strings in Python
#PEP 498 -- Literal String Interpolation
name = "Eric"
age = 74
print(f"Hello, {name}. You are {age}.")
#Python-Version:	3.6

#Arbitrary Expressions
#Because f-strings are evaluated at runtime, you can put any and all valid Python expressions 
print(f"{2 * 37}")


def to_lowercase(str):
 return str.lower()
name = "Eric Idle"
print(f"{to_lowercase(name)} is funny.")


name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
    )

print(message)

#The f in f-strings may as well stand for “fast.”