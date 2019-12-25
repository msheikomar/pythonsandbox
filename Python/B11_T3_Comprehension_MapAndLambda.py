num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = list()
for n in num:
    my_list.append(n * n)
print(my_list)

# List Comprehension
my_list = [n * n for n in num]
print(my_list)

# How to use map and lambda instead of list comprehension
my_list = map(lambda n: n * n, num)
print(my_list)  # ***********To be fixed

# Key Takeaway

# If you see map and lambda function in you code.
# It can be converted to list comprehension bcz 99% of time they can be.
# Map will run each element from the list through the function.
# Lambda is an anonymous function

