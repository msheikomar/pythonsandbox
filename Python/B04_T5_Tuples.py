# List is mutable and Tuples is immutable

# Example :1 It shows list is mutable
list_1 = ['History', 'Math', 'Physics', 'ComSys']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'


print(list_1)
print(list_2)

# Example :2 It shows Tuples is immutable
tuple_1 = ('History', 'Math', 'Physics', 'ComSys')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art' # You can not modify tuples

print(tuple_1)
print(tuple_2)




