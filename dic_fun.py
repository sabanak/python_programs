# dict1={
#     1:'abc',
#     2:'eghj',
#     3:'qwerty'
#}

#accessing an value using key
#print(dict1[2])

#changing value of an item using key
# dict1[1]='hello'
# print(dict1)

#trying to access an value using key which is not present cause keyerror
#print(dict1[4])

#Looping through dictionary
#will print all keys
# for i in dict1:
#     print(i)


#for printing all values
# for i in dict1:
#     print(dict1[i])

#checking an element using in operator
# if 1 in dict1:
#     print('available')

#checking an element using not in operator
# if 5 not in dict1:
#     print('Not available')

#checking length of dictionary
# print(len(dict1))


#FUNCTIONS:get,append,pop,delete,copy
#1:get
# dict1={
#     1:'abc',
#     2:'eghj',
#     3:'qwerty'
#}
#print(dict1.get(1))
#if an value is not availabe get produce an None object
#print(dict1.get(6))
#we can replace this none by giving string as second argument
#print(dict1.get(6,"key not found"))

#2:append or adding an element
# dict1[4]="new"
# print(dict1)

#3:pop an element
# dict1.pop(1)
# print(dict1)

#for poping last item we use popitem()
# dict1.popitem()
# print(dict1)

#4:deleting an item
# del dict1[1]
# print(dict1)

#copy a dictionary
# dict2=dict1.copy()
# print(dict2)

#creating dictionary using keyword dict
# mydic=dict(dict1)
# print(mydic)

#create a dictionary using a dict constructor
# new=dict(a="hi",b="hello",c=123)
# print(new)
# new=dict(a=[1,2,3],b="hello",c="welcome")
# print(new)

#we cant use mutable object as key
#we can use mutable object as value

#1.creating dictionary
#a,empty dictionary
dic={}
print(dic)
#b,by using dict() function
d=dict()
print(d) #it will create an empty dictionary
# d['a']=1 #we can add elements by this way
# print(d)
#2:To access elements from dictionary
#a,by using key's
# di={'a':1,'b':2,'c':3}
# print(di['a'])
# print(di['c'])
#print(di['d'])#will cause key error
#b,by using get() function
# d={'apple':'red','banana':[1,2,3]}
# print(d.get('banana'))
# print(d.get('orange')) #will return None
#3:adding elements in dictionary
# dd={'apple':1,'orange':'raw'}
# dd['banana']='yellow'
# dd['strawberry']='red'
# print(dd)
#4:Iterate through dictionary
#a,iterate over keys

#1:
d={'a':100,'b':200,'c':300,'d':400}
for key in d:
    print(key)
# #2
# d={'a':100,'b':200,'c':300,'d':400}
# for key in d.keys():
#     print(key)

#b,iterate over values
#1
# d={'a':100,'b':200,'c':300,'d':400}
# for key in d.values():
#     print(key)
# #2 this is logically equivalent to below code
# d={'a':100,'b':200,'c':300,'d':400}
# for key in d:
#     print(d[key])
#5.deleting element from dictionary
#a,pop()
# d={'a':100,'b':200,'c':300,'d':400}
# print(d.pop('b'))#200
# print(d)#{'a': 100, 'c': 300, 'd': 400}
# #b,popitem() will remove arbitrary element
# h={'a': 100, 'c': 300, 'd': 400}
# print(h.popitem())
# print(h)
# print(h.popitem())
# print(h)
# #c,clear()
# v={'a': 100, 'c': 300, 'd': 400}
# print(v.clear())
# #del keyword
# lk={'a': 100, 'c': 300, 'd': 400}
# del lk['a']
# print(lk)

#6:sorting the dictionary
# dict={'zia':4,'jeeva':8,'joju':5,'anu':9}
# student=list(dict.keys())#declared the variable student for dictionary dict #keys list['zia', 'jeeva', 'joju', 'anu']
# student.sort()#it will sort all key elements inside the dictionary dict
# for v in student:#for loop will call each key element
#     print(":".join((v,str(dict[v]))))#print string(key) and value in order
#str(dict[v]) converting value into string because we have to join key and value ,key is string
#7.setdefault()
# a,if key is not availabe
a={1:'a','apple':'fruit','banana':5}
a.setdefault('orange','raw')
print(a)#{1: 'a', 'apple': 'fruit', 'banana': 5, 'orange': 'raw'}
#b,if key is present
a={1:'a','apple':'fruit','banana':5}
print(a.setdefault('apple','rippened'))#fruit
print(a)#{1: 'a', 'apple': 'fruit', 'banana': 5}
#8.copy() for copying
a={1:'a','apple':'fruit','banana':5}
b=a.copy()
print(b)
#9:length of a dictionary
b={1:'a','apple':'fruit','banana':5}
print(len(b))
#10.update()
#a,if key is not present,the key:value will be added to dictionary
a={1:'a','apple':'fruit','banana':5}
a.update({2:'hi'})
print(a)
#b,if key is present the value will update
a={1:'a','apple':'fruit','banana':5}
a.update({1:'hello'})
print(a)
#11.cmp() will compare two dictionaries and return boolean result
dict1={1:"100",2:"200",3:"300"}
dict2={1:"200",3:"300"}
dict3={1:"100",2:"200",3:"300"}
print(dict1==dict2)#False
print(dict1==dict3)#True
#12:DICTIONARY COMPREHENSION
dict1={x:x*x for x in range(1,10)}
print('x:x*x:',dict1)
dict1={x:2*x for x in range(0,10)}
print('x:2*x:',dict1)
#13:DICTionary concatination
#a,by using update() one dictionary will merge to another
di={'a':10,'b':20,'c':30}
di1={'c':30,'d':45}
di1.update(di)
print(di1)
#b,by using **
di={'a':10,'b':20,'c':30}
di1={'c':30,'d':45}
di2={**di,**di1}
print(di2)
#14:memebership operator
#a,in
a={'b':1,'c':2}
print('b'in a )
#b, not in
print('c' not in a)
