n=int(input("enter a number : "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")

# for i in range(2,n+1):
#     if n%i==0:
#         print("not prime")
#         break
#     else:
#        print("prime")