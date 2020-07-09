

try:
    print("file operations")
    file=open('Files/july.txt','w') #read/write  w+,w,x
        
    if file.readable:
        content=file.read()
        print(content)   
    
except Exception as e:
    print('Exception is - ',e)


# compare the content in betweern files






    
    