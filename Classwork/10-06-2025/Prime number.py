#prime or not using a function
#2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
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
prime()