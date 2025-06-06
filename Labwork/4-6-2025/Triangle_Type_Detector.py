a=int(input("enter the number : "))
b=int(input("enter the number : "))
c=int(input("enter the number : "))
if a+b>c and a+c>b and b+c>a:
    print("Valid triangle")
    if a==b==c:
        print("Equilateral triangle")
    elif a==b or a==c or b==c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Invalid triangle")