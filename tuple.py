t=("apple","orange","banana")
# print(t)
#print(t[0])

#if we have to reassign a value we should convert tuple into list and reconvert it into tupple
l=list(t)
# l[1]="pineapple"
# t=tuple(l)
# print(t)
#append
# l.append("kivi")
# t=tuple(l)
# print(t)
#insert
# l.insert(1,"strawberries")
# t=tuple(l)
# print(t)

#we can perform length,count,concatination,in not in operation
#t1=(1,2,2,3,4,4,4,5,6)

#length
#print(len(t1))

#count
#print(t1.count(2))
#print(t1.count(4))

#conacatenation
t1=('a','b','c','d')
t2=(1,2,3,4,5)
print(t1+t2)

#in not in operator
if 4 in t2:
    print("present")

if 6 not in t2:
    print("not present")

#looping through tuple
for i in t1:
    print(i)

#negative indexing
t3=(1,2,3,4)
print(t3[-1])
print(t3[3])

#1.Creating tuple
#a,empty tuple
tpl=()
print(tpl)
#b,tuple without using paranthesis
tpl=100,200,300
print(tpl)
#c,tuple with using paranthesis
tpl=(100,200,300)
print(tpl)
#d,tuple with different datatypes
tpl=(1,1.2,"hi",2+3j,[1,2,3],{1,2,3},{1:'a'})
print(tpl)
#e,create tuple with nested tuple
tpl=((1,2,3),('a','b','c'),(True,False,True))
print(tpl)
#f,tuple with single element
tpl=(10,)
print(tpl)
tppl=10,#single element without paranthesis
print(tppl)
#g,by using tuple() function
tpl=tuple([1,2,3])
print(tpl)
#h,by using range function
tpl=tuple(range(100,200,4))
print(tpl)
#2,accessing elements in tuple
#a,by using positive index
tpl=(1,2,3)
print(tpl[1])
#b,by using negative indexing
tpl=('apple','oranges','banana')
print(tpl[-2])
#3.Mathematical operations on tuple
#a,+ concatenation operator
tpl=(1,2,3,4)
tpl1=(3,4,5,6)
print(tpl+tpl1)
#b,* repetition operator
tpl=('a','b','c')
print(tpl*4)
#4.Membership operator
#a,in operator
tpl=(1,2,3)
print(1 in tpl)
#b, not in operator
tpl=('hi','hello')
print('hi' not in tpl)
#5.Length of tuple
tpl=(1,2,3,4,5,5,6)#duplicates are allowed
print(len(tpl))
#6.Looping over tuple
tpl=(1,2,3,4,5,5)
for i in tpl:
    print(i)
#7.Counting elements
tpl=(1,2,3,3,3,3,4,4,5,6)
print(tpl.count(3))
#tuple packing and unpacking
#a,tuple packing
a=1
b=2
c=3
tpl=(a,b,c)
print(tpl)
#b,Unpacking
tpl=(1,2,3)
print('a=',a,'b=',b,'c=',c)
#To do operations we have to convert tuple into list
#a,reassign
tpl=(1,2,3,4)
l=list(tpl)
l[2]=88
tpl=tuple(l)
print(tpl)
#b,append
tpl=(1,2,34)
l=list(tpl)
l.append('hi')
tpl=tuple(l)
print(tpl)
#c,insert
tpl=(1,2,3,4)
l=list(tpl)
l.insert(0,'apple')
l.pop()
l.remove(2)
l.remove(1)
tpl=tuple(l)
print(tpl)
l=(1,2,3)
l1=(1,2,3)
print(l==l1)





















