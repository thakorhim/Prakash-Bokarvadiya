l=1
l1=[]
file=open("list.txt","w")
while l<31:

    file.write(str(l)+"\n")
    l1.append(l)
    l += 1
file.close()
file=open("list.txt","r")
print(file.read())
file.close()