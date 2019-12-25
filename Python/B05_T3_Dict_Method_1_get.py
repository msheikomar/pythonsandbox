# get method is used to run the code without throwing error if the key does not exists

student = {'name':'john', 'age':25, 'courses':['Math', 'CompSys']}

# To access value using key
print(student.get('name'))

# To access key that does not present in the dictionary
print(student.get('phone'))

# We can also specify the default value if the key does not exists
print(student.get('phone','Not Found'))





