courses = ['History', 'Math', 'Physics', 'ComSys']

for index,course in enumerate(courses):
    print(index,course)
print("--------------")
for index,course in enumerate(courses, start=1):
    print(index,course)