n=int(input("enter the number : "))
while n>0:
    num=n
    sum=0
    while num>0:
        rem=num%10
        sum=sum+rem**3
        num=num//10
    if sum==n:
        print(n,"is armstrong number")
    else:
        print(n,"is not armstrong number")
    break