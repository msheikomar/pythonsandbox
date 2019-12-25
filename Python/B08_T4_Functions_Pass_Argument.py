# Here function argument is mandatory. If argument is missing python throws error
def hello_func(greetings):
    return '{} Function.'.format(greetings)

print(hello_func('Hi'))

# Here in this function argument is not mandatory. Bcz we pass the default value
def hello_func_2(greetings,name = 'You'):
    return '{},{}.'.format(greetings, name)

print(hello_func_2('Hi'))
print(hello_func_2('Hi' , name = 'Corey'))

# Key Take away
#1. You require positional argument have to come before your keyword argument
#2. If you pass the argument is out of order then it will give you an error

