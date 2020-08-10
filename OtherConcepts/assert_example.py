

x=10

try:
    assert x>10,"here x value should be > 10"
except AssertionError:
    print("Condition is failed")


y=5 
assert y>5,"here x value should not be > 5"
print(y)