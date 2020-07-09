
x=2 

# string --- alphabets + numbers +special values 
complete_string='a1@'
print(type(complete_string))

print(complete_string)

name='hello'
print(name)
print(type(name))

# 4 ways - strings 

# '' 
# '' ''
# ''' ''' 
# str 

movie='Titanic'
movie_name="Titanic"
movie_name_2='''Titanic '''  # string 

print(movie)
print(movie_name)
print(movie_name_2)


news_title="corona virus breakdown- 'USA' is top postion in world"
print(news_title)

#3 ->  string, comment (multil line) and doc string classes (OOPS)

'''
 this is multi line comment. 
 this text is not executed 
  end of the text 
   print("hello")
'''

print('after multiline comment')

mobile_number=9567889705
print(type(mobile_number))

# len - length function - how many characters 

# Can we able convert complex into strings ? (str)

mobile_new=str(mobile_number)
print(mobile_new)
print(type(mobile_new))

print(len(mobile_new))


# take any int 
# str() ... int str 
# len() 


milk_litr=2.45
print(len(str(milk_litr)))



# indexing []
text='baseball'



# 0   - n-1  n= length of string  -- Fwd 
# -1 ..... -n  -back                              
print(len(text))
print(text)
print(text[2])
print(text[3])
print(text[0])
print(text[4])
print(text[7])


print(text[-1])
print(text[-5])


# slice 
# [startindex : endindex ]

# B A S E B A L L 
print(text[2:])

print(text[:4])

print(text[4:-1]) # -1 = 7 

s1=text[:2]
s2=text[5:7]

print(text[:2],text[5:7])
print(s1+s2)

firstname='Baracka'
middlename='robert'
lastname='Obama'
fullname=firstname+middlename+lastname
print(fullname)


# +, [], [:]


news='''
Hong Kong’s legislature approved a contentious bill on Thursday that makes it illegal to insult the Chinese national anthem.
The legislation was approved after pro-democracy opposition lawmakers tried to disrupt the vote. The bill was passed with 41 lawmakers voting for it and just one voting against. Most of the pro-democracy lawmakers boycotted the vote out of protest.
The pro-democracy camp sees the anthem bill as an infringement of freedom of expression and the greater rights that residents of the semi-autonomous city have compared to mainland
'''

print(news.title())


country='raja'
print(country[::-1])