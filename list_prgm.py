# list1=["a","b","c",1,2,3,4,5,8]
# print(list1)

# print(list1[0])
# print(list1[5])

# list1=[1,2,3,4,5]
# list2=[10,12,13,14]
# print(list1+list2)

# list1=["apple","orange","grapes","pineapple"]
# #print("orange" in list1)
# list1[2]="vegetables"
# print(list1)

# #list functions
# #append
# list1=["apple","orange","grapes","pineapple"]
# list1.append("xyz")
# print(list1)

# #insert
# list1=["apple","orange","grapes","pineapple"]
# list1.insert(1,"egg")
# print(list1)

#length
# list1=["apple","orange","grapes","pineapple"]
# print(len(list1))

#index
# list1=["apple","orange","grapes","pineapple"]
# print(list1.index("grapes"))

#ACCESING LIST ELEMENTS
#l=[1,2,3,4,5,6]
#ACCESING USING POSITIVE INDEX
#print(l[2])
#ACCESING USING NEGATIVE INDEX
#print(l[-2])

#ADDING ELEMENTS TO LIST
l=[1,2,3,4,5,6]
#APPEND()
# l.append(7)
# print(l)
#INSERT()
# l.insert(3,9)
# print(l)
#EXTEND()ADDING MORE THAN ELEMENTS TO THE END in the form of list
# l.extend([10,43,23])
# print(l)

#REMOVING ELEMENTS FROM THE LIST
#l=[1,2,3,4,5,6]
#REMOVE() WILL REMOVE A PARTICULAR ELEMENT
# l.remove(4)
# print(l)
#POP()WILL REMOVE ELEMENT FROM THE END
# l.pop()
# print(l)
#POP(INDEX)WE CAN POP ELEMENT BY USING INDEX
# l.pop(2)
# print(l)

#ORDERING OF A LIST
#l=[1,2,3,4,5,6]
#REVERSE()
# l.reverse()
# print(l)
#USING SLICING
#l=l[::-1]
#print(l)

#ACCESING ELEMENTS IN REVERSE ORDER
# l=[1,2,3,6,5,4,55,22,11,89,0]
#REVERSED
# print(list(reversed(l)))
#SORT syntax:sort(key= reverse=True)
#l.sort()
#print("ASCENDING ORDER",l)#output will be [0,1,2,3,4,5,6,11,22,55,89]
#l.sort(reverse=True)
#print("DESCENDING ORDER",l)#output will be [89,55,22,11,6,5,4,3,2,1,0]
#PYTHONS IN BUILT FUNCTION SORTED() WILL DO THE SAME
# l2=[70,50,60,1,20]
# print("IN ASCENDING ORDER",sorted(l2))#output will be [1,20,50,60,70]
# print("IN DESCENDING ORDER",sorted(l2,reverse=True))#output wil[70,60,50,20,1]
#ARITHMETIC OPERATIONS ON LIST
# + OPERATOR CONCATINATION
# l=[1,2,3,4,5]
# l1=[8,9,10,44]
# print(l+l1) #output will be [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# * OPERATOR REPETITION OPERATOR
# print(l*3) #output will be [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

#COMPARING LIST OBJECTS will gives an boolean output True or False
# l=[1,2,3]
# l1=[1,2,3]
# l2=[2,4,5]
# print(l==l1)
# print(l==l2)
# print(l!=l2)

#number of elements should be same
#order of elements should be same
#the contents of elemnt(case sensitive in case of string elements)

#MEMBERSHIP OPERATORS will return boolean values True or False
#l4=['a','b','c']
#in operator
# print('a' in l4)
# print('e' in l4)
#not in operator
#print('e'not in l4)

#CLEAR()USED TO REMOVE ALL ELEMENTS FROM LIST
l5=[1,2,3,4]
l.clear()
print(l)

#NESTED LIST
l6=[1,2,3,[4,5]]
print(l6[0])
print(l6[3][1])
for i in l6:
    print(i)

#LIST CREATION
#1.creating empty list
# list=[]
# print(list)
# #2.create list with elements
# l=[1,2,3,4,5]
# print(l)
# #3.dynamically create list
# # l1=eval(input("enter list"))
# # print(l1)
# #4.create list using strings
# l2=["hi how are you"]
# print(l2)
# #5.create list with more than one string elements
# l3=["apple","orange","banana"]
# print(l3)
# #6.create multi-dimensional list(nested list)
# l4=[[1,2,3,4],[4,6,7]]
# print(l4)
# #7.create a list with duplicate values
# l5=[1,3,4,4,5,6,4,5,7]
# print(l5)
# #8.create list with different datatypes
# l6=[1,'a',1.23,[1,2,3],['a','b']]
# print(l6)
# #9.CREATE LIST BY USING split() function
# s="Be a Master"
# print(s.split())  #split at space ['Be', 'a', 'Master']
# s="be,haapy"
# print(s.split(',')) #split at , ['be', 'haapy']
# s="1:2:3:4:5"
# print(s.split(':')) #split at : ['1', '2', '3', '4', '5']
# s="hello world"
# print(s.split('@')) #split at @ ['hello world']
# #max-split-max-split
# a="1,2,3,4,5,6"
# print(a.split(',', 2)) #will split first two elements ['1', '2', '3,4,5,6']
# print(a.split(',', 4)) #will split first four elements ['1', '2', '3', '4', '5,6']
#
# b="banana,orange,apple,pineapple,blueberries"
# print(b.split(',', 2))#will split first two elements ['banana', 'orange', 'apple,pineapple,blueberries']
# print(b.split(',', 4))#will split first four elements ['banana', 'orange', 'apple', 'pineapple', 'blueberries']
# print(b.split(',', 0)) #['banana,orange,apple,pineapple,blueberries']
