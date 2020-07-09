

#FileNotFoundError: [Errno 2] No such file or directory: 'Files/Sample.txt'
file=open('Files/Sample.txt','r+')
print(file.name)
print(file.readable())
print(file.writable())
#file.close()
print(file.closed)
print(file.mode)
