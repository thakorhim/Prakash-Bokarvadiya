i=0
ev=0
odd=0
evsum=0
oddsum=0
while(i<5):
    num=int(input("Enter the number : "))
    if(num%2==0):
        print("Even number:",num)
        ev=ev+1
        evsum=evsum+num
    else:
        print("Odd number:",num)
        odd=odd+1
        oddsum=oddsum+num
    i=i+1
print("Even Number : ",ev)
print("Odd Number : ",odd)
print("Even sum : ",evsum)
print("Odd sum  : ",oddsum)