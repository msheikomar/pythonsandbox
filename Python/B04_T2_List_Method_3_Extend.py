# To merge two different list
courses = ['History', 'Math', 'Physisc', 'CompSys']
courses_2=['Art', 'Education']

# **This approach will insert list inside the list. But this not the one we expected
#courses.insert(0,courses_2)
#print(courses)
#print(courses[0])

# **This approach will insert list at end of  the list. But this not the one we expected
#courses.append(courses_2)
#print(courses)


# The solution is use extend() method
print("Example to Use extend() method")
courses.extend(courses_2)
print(courses)
