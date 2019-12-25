di = {'name':'Corey','job':'programming','age': None, 'os':'Mac'}
s_di = sorted(di) # This will sort the Keys and return the list
print(s_di)

#AttributeError: 'dict' object has no attribute 'sort'
s_di = di.sort()


