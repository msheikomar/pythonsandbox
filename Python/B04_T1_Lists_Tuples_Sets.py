# Lists and Tuples allows us to work with sequential data
# Sets are unordered collections of values with no duplicate

# List Example
courses = ['History', 'Math', 'Physics', 'ComSys']  # Create List with elements
print(courses)  # To print lists
print(len(courses))  # To print length of list
print(courses[0])  # To access first value from the list
print(courses[3])  # To access last value from the list

# We can use -ve index too to access last value of the list
print("-ve index example")
print(courses[-1])  # So zero is the first item of the list -1 is the last item of the list

# List index error
# print(courses[4])  # **List index out of range

# Get first two values/items from the list
print("Get first two values/items from the list")
print(courses[0:2])
print(courses[:2])  # Alternative approach. You can leave off the start index as empty

# Get  values/items from the mid of the list and all the way end
print(courses[2:])  # Leave the end index empty


