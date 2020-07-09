import os


print(os.name)#java,ce,os2,riscos,nt 
print(os.getcwd())
try: 
   print(os.mkdir('testdir'))
except (FileExistsError,FileNotFoundError) as fe:
    print("Error is - ",fe)
finally:
    os.rmdir('testdir')
    
    
file_obj=open("Modules2/file.txt",'a') 
file_obj.write("hello this is python script. added text")
file_obj.close()
if file_obj.closed:
    print('file is closed')
    
#print(os.chdir(".."))
    
#print(os.getcwd())

#os.rename('ABCDE.txt','XYZ.txt')

print(os.cpu_count())

print(os.environ)
print(os.access('Modul/file.txt',os.F_LOCK))


wheel files 
pyinstaller 


watchdog
shutil
pathlib 

selenium 
chrome webdriver 

host name 
user 
pwd 








