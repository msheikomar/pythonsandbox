# Sets: values are unordered and no duplicates
# Sets don't really care about the order. SO the output will change each execution
# Uses: Set is used to test whether a value is part of a set(Membership Test) and also it's used a lot to remove duplicate values

courses = {'History', 'Physisc', 'Math', 'ComSys','Math'}

# If we add math into the set which is duplicate so python will remove it

print(courses)

# Membership test. We can use this lists and Tuple but set is fast
print('Math' in courses)




