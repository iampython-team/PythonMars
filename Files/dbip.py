ipfile=open('Files/ip.txt','r')
dbfile=open('Files/db.txt','r')
# ipfile.writelines("192.178.80.1\n")
# ipfile.writelines("192.178.80.2\n")
# ipfile.writelines("192.178.80.3\n")
# ipfile.writelines("192.178.80.4\n")
# ipfile.writelines("192.178.80.5\n")
# ipfile.writelines("192.178.80.6\n")

# dbfile=open('Files/db.txt','w+')
# dbfile.writelines("PrePROD\n")
# dbfile.writelines("UAT\n")
# dbfile.writelines("TEST\n")
# dbfile.writelines("DEV\n")
# dbfile.writelines("DEV2\n")
# dbfile.writelines("Regression\n")

#listx=[ (ipcontent,dbcontent) for ipcontent in ipfile.readlines() for dbcontent in dbfile.readlines() ]
#print(listx)
#trim() 
listx=[ (ipcontent+dbcontent).replace('\n','@',1).strip() 
        for ipcontent,dbcontent in zip(ipfile.readlines(),dbfile.readlines()) ]
#print(*listx,sep='\n')
for i in listx:
    print(i)
    
    
evennumbers=[2,4,6,8,10]
oddnumbers=[1,3,5,7,9]
primenumbers=[2,3,5,7,11]
print(list((zip(evennumbers,oddnumbers,primenumbers))))
 
 

file=open('Files/phone.properties','w')
for i in range(10):
    file.write(str(i))
file.close()
 
#.properties 
#.conf -- Python DB 


    







