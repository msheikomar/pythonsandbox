li = [8,7,6,9,3,2,5,4,1]
print(li)

# To sort without impacting the ordinal list use sorted() function
s_li = sorted(li) # Create new variable to see the results
print('Sorted Variable:', s_li)


# To sort original list without using new variable use sort() method
li.sort()
print('Original Variable:', li)

# Difference between sorted() function and sort method
# Key Take away is sorted() function gives new sorted list and the sort function perform sort inplace

s_li = li.sort()
print(s_li)

# Sort in descending order
s_li = sorted(li,reverse=True)
li.sort(reverse=True)
