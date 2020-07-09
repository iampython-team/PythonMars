# vargs variable args
def display_student_names(names):
    print(names)

display_student_names('raja')
display_student_names('Ajay')
display_student_names('Ajeet')

def display_student_names(*names):
    print(names)
    print(type(names))

display_student_names('raja','Ajay',56,[1,2,3],3+4j)

# kwargs keyword args

def person(**persondata):
    print(persondata)
    print(type(persondata))
    
person(name='Raja',age=45)
person(name='xyz',age=32)

def all_data(name,*lang,country='USA',**bookauthours):
        print(name,lang,bookauthours,country)
        
all_data('John','English','Spanish','Italian',book1='auth1',book2='auth2')


