#factorial

def factorial(n):
    #n=10
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        #1=1*1    i=1
        #1=1*2    i=2
        #2=2*3    i=3
        #6=6*4    i=4
    print("factorial of",n,"is",fact)
#fibonacci
def fibonacci(n):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
#prime number
def prime(n):
    #n=10
    count=0
    for i in range(1,n+1):
        #i=1
        #i=2
        #i=3
        #i=4
        #i=5
        if n%i==0:
            count=count+1
            #0=0+1
            #1=1+1
            #count=2

    if count==2:
        print(n,"is prime number")
    else:
        print(n,"is not prime number")

#armstrong number

def armstrong(n):
    temp=n
    sum=0
    while n>0:
        r=n%10
        sum=sum+(r*r*r)
        n=n//10
    if temp==sum:
        print(temp,"is armstrong number")
    else:
        print(temp,"is not armstrong number")

#main
while True:
    print("1.factorial")
    print("2.fibonacci")
    print("3.prime number")
    print("4.armstrong number")
    print("5.exit")
    #choice
    ch=int(input("enter your choice :"))
    #function calling
    if ch==1:
        n=int(input("enter a number"))
        factorial(n)#factorial function calling
        print("---------------------------------")
    elif ch==2:
        n=int(input("enter a number"))
        fibonacci(n)#fibonacci function calling
        print("---------------------------------")
    elif ch==3:
        n=int(input("enter a number"))
        prime(n)#prime function calling
        print("---------------------------------")
    elif ch==4:
        n=int(input("enter a number"))
        armstrong(n)
        print("---------------------------------")
    elif ch==5:
        print("thank you")
        break
    else:
        print("invalid choice")