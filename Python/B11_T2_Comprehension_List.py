num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []
for n in num:
    my_list.append(n*n)
print(my_list)

# Complex List comprehension example

my_list = [n*n for n in num]
print(my_list)