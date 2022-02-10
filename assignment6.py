#1:WRITE MODE
file=open('demo.txt','w')
file.write("HELLO")
file.close()

#2:READ MODE
file=open('demo.txt','r')
contents=file.read()
print(contents)
file.close()

#3:APPEND MODE
file=open('demo.txt','a')
file.write("\nHow Are You?")
file.close()