# Generators, why?
# Some of the advantages over list. It loop through all the numbers we passed in


def square_numbers(num):
    result = []
    for i in num:
        result.append(i * i)
    return result


my_nums = square_numbers([1, 2, 3, 4, 5])
print(my_nums)

# How to convert this square_number() function to a generator
# 1)Remove the empty list
# 2)Remove the return statement
# 3)Remove the append method by the key word 'Yield'


def square_numbers1(num):
    for i in num:
        yield (i * i)


my_nums1 = square_numbers1([1, 2, 3, 4, 5])
print(my_nums1)
for i in my_nums1:
    print(i)

