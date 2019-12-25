num = [1,2,3,4,5,6,7,8,9,10]

my_list=[]
for n in num:
    if n%2 == 0:
     my_list.append(n)
print(my_list)

# Complex List comprehension example

my_list = [n for n in num if n % 2 == 0]
print(my_list)

#Filter and lambda function

my_list = filter(lambda n: n%2 == 0, num)
print(my_list)# To be fixed

# Key Takeaway
# We have filter function. Filter, it runs the list through this function and only gives us the values are even.

