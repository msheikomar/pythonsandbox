# It allowing us accept an arbitrary number of positional or keyword arguments

def student_info(*args, **kwargs):
    print(args)  # Result is Tuples
    print(kwargs)  # Result is Dict

student_info('Math','Art', name = 'John', age = 22)

print('------------------')
def student_info_2(*args, **kwargs):
    print(args)  # Result is Tuples
    print(kwargs)  # Result is Dict

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info_2(*courses, **info)


