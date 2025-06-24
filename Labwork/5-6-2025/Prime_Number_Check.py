n=int(input("Enter a number:"))
while n>0:
    num=n
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print(n,"is a prime number")
    else:
        print(n,"is not a prime number")
    break