#choice through function coll
from random import choice


def prime():
    n=int(input("enter a number : "))
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print("prime")
    else:
        print("not prime")
def fact():
    n=int(input("enter a number : "))
    fact=1
    while n>0:
        fact=fact*n
        n=n-1
    print(fact)
def pattern1():
    for i in range(1,5):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
while True:
    print("1.prime or not")
    print("2.factorial")
    print("3.pattern")
    print("4.exit")
    choice=int(input("enter your choice : "))
    if choice==1:
        prime()
    elif choice==2:
        fact()
    elif choice==3:
        pattern1()
    elif choice==4:
        break
    else:
        print("invalid choice") 