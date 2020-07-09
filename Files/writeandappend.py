
file=open('Files/test2.txt','x',encoding='UTF-8')
file.write("This is my first comment. this is my second comment")
file.close()

# w/a - create a new file if file is not exists 
# w/a - it will not throw any error if file is already exists 
# w/a - w mode - overwrite 
#       a mode - add the content at the EOF


# x -FileExistsError: [Errno 17] File exists: 'Files/test.txt'


