#filter function
#in the case of filter there will be a condition has to be check
#syntax filter(function,sequence)
list1=[1,2,3,4,5,6]
list2=list(filter(lambda x:x%2==1,list1))
print(list2)

#here filter will pass values from list1 to lambda
#and filter will return all the true results return by lambda
#and we print it in a list