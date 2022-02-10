#map function
#syntax: map(function,sequence)
list1=[1,2,3,4,5,6,7]
list2=list(map(lambda x:x*2,list1))
print(list2)

#map function will take two parameters lambda as function and
#list1 as sequence.Here map function will pass each value in the list to
#lambda function and return the results returned by lambda