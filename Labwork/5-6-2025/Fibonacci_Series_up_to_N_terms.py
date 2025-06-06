num = int(input("Enter a number: "))
i=0
a=1
sum=0
print("Fibonacci series is:")
while i<=num:
    print(sum,end=" ")
    sum=i+a   
    i=a
    a=sum
    


