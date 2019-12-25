# List Comprehension using nested for loop
my_list = []

for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)

my_list1 = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list1)

