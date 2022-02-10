#1:set creation
# setx=set()#empty set
# print(setx)
# nums=[1,2,3,4,6]#with elements
# print(set(nums))
#2.adding elements to set
# num={1,2,3,4,5}
# num.add("hi") #can add one element
# print(num)
# #3:update set
# nums={1,2,3,4}
# nums.update([9,5,4]) #can add more elements
# print(nums)
#4:removing elements from set
#a,pop()
# n={1,2,3,4,5}
# n.pop()
# print(n)
# n.pop()
# print(n)
#
# #b,remove()
# m={1,2,3,4,5,6}
# m.remove(2)
# print(m)
# m.remove(7)
# print(m)
#
# #c,discard()
# l={1,2,3,4,5,6}
# l.discard(4)
# print(l)
# l.discard(7)
# print(l)

#5:length of a set
d={1,2,3,4,5,6,7,8}
print(len(d))

#6:memebership operation
a={1,2,3,4}
print(1 in a)
print('a' not in a)

#7:eliminating duplicate elements
f={1,2,2,2,3,4,4,5,6}
print(f)

#8:clear a set
b={1,2,3,4}
b.clear()
print(b)

#9:mathematical operation
# first={1,2,3,4,5,6}
# second={1,2,4,7,8,9}
# print(first | second)
# print(first & second)
# print(first-second)
# print(second-first)
# print(first^second)

#converting other types to set using set()
k=1,2,3,4,5,6
h="hihowareyou"
ff=1.2,1.45
ll=[1,2,3,4]
print(set(k))
print(set(h))
print(set(ll))
print(set(ff))


s
