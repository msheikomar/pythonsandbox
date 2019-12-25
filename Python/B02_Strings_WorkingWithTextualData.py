# Begginner 2 : Strings - Working with Textual Data
# Tips 1: Use backslash(\) to escape single quote in string
# Tips 2: Multiline String use triple quote (""")

message = "Hello World"
print(len(message))  # To find length of the string
print(message[0])  # To access first character of the string
print(message[10])  # To access any char of string
# print(message[11])  # **To get index out of range exception
print(message[0:5])  # To get range of char(first 5 char) from string
print(message[:5])  # Alternate way to get first five char of string
print(message[6:])  # To get char from mid of the string and all the way to the end
print(message.lower())  # To lower case the string
print(message.upper())  # To upper case the string
print(message.count('Hello'))  # To count certain number of char in the string.Use count method.This method takes string as a argument
print(message.count('l'))  # To get number of times 'L'present in the string
print(message.find('World'))  # To find index of certain char use find method
print(message.find('Universe'))  # To find the index of char does not exists will get negative index
new_message = message.replace('World', 'Universe')  # To replace old string with new string
print(new_message)

message1 = "HELlo WORLD"
print(message1.title())
