li = [-6,-5,-4,1,2,3]
s_li = sorted(li) # Default sort
print(s_li)

s_li = sorted(li,key=abs)# It run each element through this abs function
print(s_li)

# Key Take away
# Key parameter is extremely useful when you sort named attributes