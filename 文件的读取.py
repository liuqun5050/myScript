# a = open("aa.txt","w")
# a.write("你好")
# a.close()
a = open("aa.txt","a")
b = a.write("hello world")
print(b)
a.close()

a =  open("aa.txt","r")
b = a.read()
print(b)
a.close()  