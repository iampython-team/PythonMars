

file=open('Files/nocontent.txt','r')
#file.write('This is July month. year 2020')
print(file.tell())
print(file.seekable())
file.seek(3,0)  # offset, when
print(file.seekable())
print(type(file.read()))
print(file.tell())
print(file.seekable())
file.close()
#print(file.seekable())

# offset - negative, positive int - - n +n 
# from_what 
# 0 - starting the file 
# 1 - current position
# 2 - end of file 
