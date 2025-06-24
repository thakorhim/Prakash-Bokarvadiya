#function with parameter and return type
#factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
#prime number
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False

#main

while True:
    print("1.factorial")
    print("2.prime number")
    print("3.exit")
    #choice
    ch=int(input("enter your choice:"))
    #function calling
    if ch==1:
        n=int(input("enter a number"))
        factorial(n)#factorial function calling
        print("factorial of",n,"is",factorial(n))
    elif ch==2:
        n=int(input("enter a number"))
        result=prime(n)#prime function calling
        if result==True:
            print(n,"is prime number")
        else:
            print(n,"is not prime number")
    elif ch==3:
        print("thank you")
        break
    else:
        print("invalid choice")
