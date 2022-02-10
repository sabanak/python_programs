#a program for finding squares
# def square():
#     for i in range(10):
#         print(i*i)
# square()
#
 #we can simply write it by list comprehension
# li=[i*i for i in range(10)]
# print(li)

#example 2
# letters=[]
# for i in "avodha":
#     letters.append(i)
# print(letters)

#by list copmprehension
# letters=[i for i in "avodha"]
# print(letters)


#example 3
# even=[]
# for i in range(10):
#     if i%2==0:
#         even.append(i)
# print(even)

#by list comprehension
# even=[i for i in range(10) if i%2==0]
# print(even)

#list comprehension for power of numbers of even numbers
list=[1,4,5,8]
even=[i**2 for i in list if i%2==0]
print(even)

#list comprehension for power of numbers of odd numbers
list=[1,4,5,8]
odd=[i**2 for i in list if i%2!=0]
print(odd)