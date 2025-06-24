a= int(input("Enter the number :"))
b= int(input("Enter the number :"))
operator=input("Enter the operator :")
if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    if b==0 or a==0:
        print("Division by zero is not possible")
        
    else:
        print(a/b)
else:
    print("Invalid operator")   