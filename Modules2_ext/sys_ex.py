import sys 
import logging

logging.info("hello")

print(sys.version)
#print(sys.modules) # count of modules 
print("=======")
for i in sys.argv:
    print(i)
print("=======")
print(sys.path)
print(sys.copyright)
print(sys.api_version)
print(sys.base_prefix)
print(sys.maxsize)

print("before exit")
print(sys.exit(0))
print("after exit")


