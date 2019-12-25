

student = {'name':'john', 'age':25, 'courses':['Math', 'CompSys']}

#Tip 1: This method will remove the key/value
#del student['age']
#print(student)

#Tip 2: This method will remove the key/value and return value

age = student.pop('age')
print(student)
print(age)


