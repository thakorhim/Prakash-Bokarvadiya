n1=int(input("Enter the number :"))
n2=int(input("Enter the number :"))
n3=int(input("Enter the number :"))
n4=int(input("Enter the number :"))  
if n1>n2 and n1>n3 and n1>n4:
    print(n1," is greatest")
elif n2>n1 and n2>n3 and n2>n4:
    print(n2," is greatest")
elif n3>n1 and n3>n2 and n3>n4:
    print(n3," is greatest")
else:   
    print(n4," is greatest")