#STRING FUNCTIONS

# newstring="Hello world"
#
# #endswith
# print(newstring.endswith("world"))
#
# #startswith
# print(newstring.startswith("Hello"))
#
# #uppercase
# print(newstring.upper())
#
# #lowercase
# print(newstring.lower())
#
# #join
# l=['me','you','we']
# print(",".join(l))
#
# #replace
# string="hello me"
# print(string.replace("me","world"))
#
# #split
# string="hi,how,are,you"
# print(string.split(","))
# #count()
# s="hi hi am good"
# print(s.count("am"))
# print(s.count("o",0,12))
# #find() will find first occurances of specified element
# m="hi how are you"
# print(m.find("i"))
# print(m.find("w"))
# print(m.find("o",5,13))
# #rfind will find last occurances of specified element
# v="am sabana from calicut"
# print(v.rfind("a"))
# #capitalize() will return first caharacter in upper case
# l="hi how are"
# print(l.capitalize())
# #title() will return frist alphabet of every elemnt in upper case
# print(l.title())
# #lower()
# k="HI HOW"
# print(k.lower())
# #upper
# j="hi how"
# print(j.upper())
# #swapcase() will reverse upper to lower and lower to upper
# f="Hi HoW aRe"
# print(f.swapcase())
# #islower() #will return True if a string is in lower case otherwise False
# g="is lower"
# f1="IS lower"
# print(g.islower()) #True
# print(f1.islower()) #False
# #isupper() will return True if a string is in upper case otherwise False
# lll="HI HOW ARE YOU"
# kkk="hi HOW are you"
# print(lll.isupper())
# print(kkk.isupper())
# #istitle() will return True if each word in a string begins with uppercase otherwise False
# hh="Hi How"
# ss="Hi how"
# print(hh.istitle())
# print(ss.istitle())
# #replace() will replace a string with substring
# aa="hi how are you"
# print(aa.replace("hi","hello"))
# #strip() will remove extra space at the beggining and end
# sd="      mango    "
# print("hi",sd.strip(),"hello")
# #lstrip() removes space at the left of the string
# hhh="       mango is    "
# print("the fruit ",hhh.lstrip(),"very tasty") #the fruit  mango is     very tasty
# #rstrip() will remove space from right
# print("the fruit",hhh.rstrip(),"is very tasty")#the fruit        mango is is very tasty
# #partition() of will search a string and resulting string in the format of tupple
# eg="hi how are you"
# print(eg.partition("how")) #resulting tuple ('hi ', 'how', ' are you')
# print(eg.partition("me")) #('hi how are you', '', '')
# #join()will join string elements syntax:.join(iterable)
# fh=["hi","how","are"]
# print(''.join(fh))#hihoware
# print(','.join(fh))#hi,how,are
# print(':'.join(fh))#hi:how:are
# print('@'.join(fh))#hi@how@are
# #isspace() will return True if string is space
# jju=""
# print(jju.isspace()) #False
# jjuu="  "
# print(jjuu.isspace()) #True
# #isalpha() will return True if string conatain alphabets
# lo="hihowareyou"
# loo="hi how are you" #is white space is there it will be False
# lo1="is 123"
# print(lo.isalpha()) #True
# print(loo.isalpha()) #False
# print(lo1.isalpha()) #False
# #isdigit() will return True if it's digit
# kk="1234"
# print(kk.isdigit()) #True
# kkk="123 123"
# print(kkk.isdigit()) #False white space
# #isalnum() will return True if string is alphanumeric a-z and 0-9
# lkj="123ghj A"
# print(lkj.isalnum()) #False there is white space
# lkjj="123ghjA"
# print(lkjj.isalnum()) #True
# #startswith()
# my="hi how are you"
# print(my.startswith("hi")) #will return true
# #endswith()
# we="how are you"
# print(we.endswith("you")) #true
# #encode() #encodes given string with specified encoding otherwise utf-8 will be used
# #syntax:encode(encoding=encoding,errors=errors)
# jkl="style"
# print(jkl.encode(encoding="ascii",errors="namereplace"))
# #decode() #used to decode
#
#NUMERIC FUNCTIONS
# print(min(1,2,3,0,11,3))
# print(max(1,2,3,4,11,33,22))
# print(abs(-22))
# print(sum([1,2,3,4,5,6]))
# print(pow(2,3))
# print(eval('12+11'))
# print(round(3.145677,2))
# print(round(3.145789,1))
# print(int("1234"))
#
# #random numbers
# import random
# print(random.random())
# print(random.random())
# #choice() using choice() to generate random number from a list
# print(random.choice([1,2,3,4,5,6]))
# #randrange() will generate random number within a range randrange(beg,end,step)
# print(random.randrange(1,19,3))
# #ceil
# import math
# print(math.ceil(300.11))
# print(math.ceil(-23.11))
# #floor
# print(math.floor(300.11))
# print(math.floor(-23.11))
# #sqrt
# print(math.sqrt(9))
#
#LIST FUNCTIONS

#all take list as an argument
nums=[1,2,3,4,5]
if all([i<6 for i in nums]):
    print("all less than 6")

#any take list as an argument
nums=[1,2,3,4,5]
if any([i%2==0 for i in nums]):
    print("at lest one is even")

#enumerate iterate over list through value and indices
nums=[1,2,3,4,5,6]
for v in enumerate(nums):
    print(v)

ad=""" hey how are
you am here to save 
you"""
print(ad)