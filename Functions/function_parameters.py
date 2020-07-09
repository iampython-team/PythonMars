
#  Function Parameters/Arguments

# types (4)

# Postional arguments/params or Required args/params #required positional argument
# Default arguments/params 
# Variable Length args  *vargs
# Keyword Args  **kwargs


def add(x,y,z=10):
    print(x+y+z)
    
add(4,5,7)


# area of cube l*b*h
def areaofcube(l,h,b=10):  #non-default argument follows default argument
    area=l*b*h
    print(area)

areaofcube(2,4,5)