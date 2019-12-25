names = ['karthik', 'Priya', 'Sethu', 'Dhana']
courses = ['ECE', 'EEE', 'CSE', 'MBA']

# Definition:Python zip is a container that holds real data inside. Python zip function takes iterable elements as input, and returns iterator.
# If Python zip function gets no iterable elements, it returns an empty iterator.

print(zip(names, courses)) #**This should print the list of tuples instead of object. As a workaround writing the below for loop 

for n in zip(names, courses):
    print(n)

# I want a dict{'name': 'courses'} for each name,courses in zip(name,courses)
my_dict = {}
for name, course in zip(names, courses):
    my_dict[name] = course
print(my_dict)

# Dict comprehension
my_dict = {name: course for name, course in zip(names, courses)}
print(my_dict)

# filter in Dict comprehension
my_dict = {name: course for name, course in zip(names, courses) if name != 'karthik'}
print(my_dict)