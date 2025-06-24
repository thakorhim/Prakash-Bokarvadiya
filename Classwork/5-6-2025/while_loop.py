# countinue number and Reverse number  print

n=int(input("Enter the number :"))
i=int(input("Enter the number :"))
if n>i :
    print("Reverse number :",n,"to",i,"is :")
    while n>=i :
        print(n,end=" ")
        n=n-1
else :
    print("countinue number :",n,"to",i,"is :")
    while n<=i :
        print(n,end=" ")
        n=n+1
