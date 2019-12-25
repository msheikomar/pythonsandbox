# This method will return the sorted version of the list as a result and the original list remains same

coueses = ['History', 'Math', 'Physics', 'CompSys']
num=[3, 1, 5, 4, 8, 7, 9]

# Sorted method does not sort the original list in place
sorted(coueses)
sorted(num)
print(coueses)
print(num)
# Store the results in temp variable
print("The value of sorted_cources is :")
sorted_cources = sorted(coueses)
print(sorted_cources)