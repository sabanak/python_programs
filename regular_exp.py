#1.match
# import re
# pattern=r"avodha"
# if re.match(pattern,"avodha are you....stay safe....."): #pattern matching pattern should give at the beggining of string
#     print("matched")
# else:
#     print("not matched")

#2.search
# import re
# pattern=r"avodha"
# if re.search(pattern,"hihihowareavodhahi"):
#     print("matched")
# else:
#     print("not matched")

#3.findall
# import re
# pattern=r"avodha"
# print(re.findall(pattern,"hiavodha avodha howavodha areyou"))kl


#4.sub(find and replace)
# import re
# str="hi avodha, how are you"
# pattern=r"avodha"
# print(re.sub(pattern,"AVODHA NEW",str))

#5. dot meta character
# import re
# pattern=r"av.d.a"
# if re.match(pattern,"avodka"):
#     print("matched")
# else:
#     print("not matched")

#6.character class
# import re
# pattern=r"[A-Z][a-z][0-9]"
# if re.search(pattern,"Av3"):
#     print("correct")
# else:
#     print("not correct")

#REGEX SEARCH
# import re
# pattern=r"pam"
# match= re.search(pattern,"sdfpamfg")
# if match:
#     print(match.group())
#     print(match.start())
#     print(match.end())
#     print(match.span())
#
#SEARCH AND REPLACE
# import re
# str="hi amrutha how are you"
# pattern=r"amrutha"
# print(re.sub(pattern,"aswathy",str))
#
# number=input("enter number")
# pattern=r'00'
# print(re.sub(pattern,'+',number))

#metacharacter
#1.'.' metachracter
# import re
# pattern=r"sa.ana"
# if re.match(pattern,"sabana"):
#     print("matched")
# if re.match(pattern,"blue"):
#     print("matched")
# else:
#     print("not matched")

#2. '^' and '$'
# import re
# pattern=r"^sab.na$"
# if re.match(pattern,"sabana"):
#     print("matched")
# if re.match(pattern,"zabZna"):
#     print("matched")
# if re.match(pattern,"sabXnm"):
#     print("matched")
# else:
#
#     print("not matched")

# word=input("enter word")
# pattern=r"^m..e$"
# if re.match(pattern,word):
#     print("matched")
# else:
#     print("not matched")

#3. '*' metacharacter

#4. '+' metacharacter
# import re
# pattern=r"g+"
# if re.match(pattern,"g"):
#     print("matched 1")
# if re.match(pattern,"ggggg"):
#     print("matched 2")
# if re.match(pattern,"ghhjdd"):
#     print("matched 3")
# if re.match(pattern,"abc"):
#     print("matched 4")
# else:
#     print("not matched")

#5.'?' metacharacter
# import re
# pattern=r"ice(-)?cream"
# if re.match(pattern,"icecream"):
#     print("matched 1")
# if re.match(pattern,"ice-cream"):
#     print("matched 2")
# if re.match(pattern,"ice--cream"):
#     print("matched 3")
# else:
#     print("not matched")

#6.'{ }' curly braces
#import re
# pattern=r"9{1,3}$"
# if re.match(pattern,"9"):
#     print("matched 1")
# if re.match(pattern,"99"):
#     print("matched 2")
# if re.match(pattern,"999"):
#     print("matched 3")
# if re.match(pattern,"9999"):
#     print("matched 4")
# else:
#     print("not matched")

#7.'|' or metacharacter
# import re
# pattern=r"gr(a|e)y"
# if re.match(pattern,"gray"):
#     print("matched 1")
# if re.match(pattern,"grey"):
#     print("matched 2")
# if re.match(pattern,"griy"):
#     print("matched 3")
# else:
#     print("not matched")
# import re
# password=input("enter password")
# pattern=r"^(a)?982{1,2}....(h)+$"
# match= re.match(pattern,password)
# if match:
#     print("password created")
# else:
#     print("not created")

#CHARACTER CLASSES
#1.
# import re
# pattern=r"[aeiou]"
# if re.search(pattern,"grey"):
#     print("matched 1")
# if re.search(pattern,"quwertykey"):
#     print("matched 2")
# if re.search(pattern,"hjklhjklm"):
#     print("matched 3")
# else:
#     print("not matched")
#
#2.with multiple classes
# import re
# pattern=r"[A-Z][A-Z][0-9]"
# if re.search(pattern,"AA3"):
#     print("matched 1")
# if re.search(pattern,"SD9"):
#     print("matched 2")
# if re.search(pattern,"aa8"):
#     print("matched 3")
# else:
#     print("not matched")
#

#3. '^' place this at the beginning to invert it
# import re
# pattern=r"[^A-Z]"
# if re.search(pattern,"this is happy time"):
#     print("matched 1")
# if re.search(pattern,"Hiit'sMeAMruTha123"):
#     print("matched 2")
# if re.search(pattern,"HIHOWAREYOU"):
#     print("matched 3")
# else:
#     print("not matched")

# import re
# student_id=input("enter id")
# pattern=r"[A-D][1-5][3-4][6-9][1-7]"
# if re.search(pattern,student_id):
#     print("Searching....")
# else:
#     print("Wrong Format")

#GROUPS
# import re
# pattern=r"a(bc)(de)(f(g)h)i"
# match=re.search(pattern,"abcdefghijklmnop")
# if match:
#     print(match.group())
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group(3))
#     print(match.groups())

#SPECIAL GROUPS
# import re
# pattern=r"(?P<first>abc)(?:def)(ghi)"
# match=re.search(pattern,"abcdefghi")
# if match:
#     print(match.group("first"))
#     print(match.groups())

#SPECIAL SEQUENCES
#1.'\1'
# import re
# pattern=r"(.+) \1"  #(.+) means 1 or more of any character,\1  means repetition of what was found in group 1
# match=re.match(pattern,"ab ab")
# if match:
#     print("matched 1")
# match=re.match(pattern,"word word")
# if match:
#     print("matched 2")
# match=re.match(pattern,"adb abv")
# if match:
#     print("matched 3")
# else:
#     print("not matched 3")
#2.\d \D \s \S \w \W
# import re
# pattern=r"(\D+\d)"
# if re.match(pattern,"a 123"):
#     print("matched 1")
# if re.match(pattern,"123 adg"):
#     print("matched 2")
# else:
#     print("not matched 2")

#3.'\A'
# import re
# pattern=r"\Asabana"
# if re.search(pattern,"sabana"):
#     print("matched 1")
# if re.search(pattern,"sssabana"):
#     print("matched 2")
# else:
#     print("not matched 2")

#4.'\Z'
# import re
# pattern=r"sabana\Z"
# if re.search(pattern,"hisabana"):
#     print("matched 1")
# if re.search(pattern,"sabanaaa"):
#     print("matched 2")
# else:                                       ]
#     print("not matched 2")
#
#5.'\b'
# import re
# pattern=r"\b(sabana)\b"
# if re.search(pattern,"asabana"):
#     print("matched 1")
# if re.search(pattern,"%% sabana ))"):
#     print("matched 2")
# else:
#     print("not matched 2")

#6.'\B'
import re
pattern=r"\B(sabana)\B"
if re.search(pattern,"sssabanagh"):
    print("matched 1")
if re.search(pattern,"123sabana223"):
    print("matched 2")
if re.search(pattern,"**sabana**"):
    print("matched 3")
else:
    print("not matched 3")