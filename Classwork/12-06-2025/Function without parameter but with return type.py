#Function  parameter but with return type
def factorial():
    num=int(input("Enter the number:"))
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

print("Factorial of given number is:",factorial())