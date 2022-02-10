#reduce function
#different from map and filter
#produce a value as output instead of list
#and it takes results of previous operation as first argument of next operation
#syntax reduce(function,sequence)
from functools import reduce
list1=[2,3,4,5]
list2=reduce(lambda x,y:x*y,list1)
print(list2)

#x,y=2,3=6
#x,y=6,4=24
#x,y=24,5=120