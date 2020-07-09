result=0
try: 
    a=3
    result=a/5
except:
    print('Exception is thrown')
else: 
    result=result+5
    print(result)
    print('else code')
finally:
    print('finally block')
    

    