dic={"Apple":200,"Orange":300,"Banana":290}
print(dic)
print(dic["Apple"]) #For getting value of key
for i in dic: #Will get keys
    print(i)
for i in dic.values(): #will get values
    print(i)
for i in dic.keys():#will get keys
    print(i)
for i in dic.items():#will get key:value
    print(i)

#for changing values
dic["Apple"]=380
print(dic)

#for deleting an item
del dic["Apple"]
print(dic)




