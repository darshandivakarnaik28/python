list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# Use zip() to combine multiple lists into a single iterable  
zipped = zip(list1,list2)
print(list(zipped))   

# Use filter() with lambda function 
# to filter out numbers less than or equal to 2 in list1  
filtered =filter(lambda x:x<=2,list1)
print(list(filtered))

# Using map() with lambda function 
# to multiply each number of list1 by 2 
mapped = map(lambda x:x*2,list1)
print(list(mapped))
