a = [1,2,3]
b = [1,2,3]

print(a == b) # This compare A and B are equal. Yes it is.

print(a is b) # This compare object A and object B using same memory location. No its is not.
print(id(a))
print(id(b))

# If you assign object B = object A then it prints True
print('-----------')
b = a
print( a is b) # Now it prints True. Bcz sharing same memory
print(id(a))
print(id(b))
print( a == b) # Yes

# Alternate way to replace 'is' operator
print('-----------')
print(id(a) == id(b)) # It print True

