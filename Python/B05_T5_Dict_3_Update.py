student = {'name':'john', 'age':25, 'courses':['Math', 'CompSys']}

# Tip 1: without using update method
#student['name']='karthik'
#print(student)

# If you want to update multiple values you can used update() method
# Update method takes in dict as an argument. So you can update the values and add new key/value in one sort

student.update({'name':'karthik', 'age':26, 'phone':'555-5555'})
print(student)
