# #swapping
# a=int(input("Enter Number A : "))
# b=int(input("Enter Number B : "))
# temp=a
# a=b
# b=temp
# print("After swapping A  : ",a)
# print("After swapping B : ",b)

# """
# a,b=b,a
# print("After swapping A  : ",a)
# print("After swapping B : ",b)

# """

#without using temp variable
x=int(input("Enter Number x : "))
y=int(input("Enter Number y : "))

x=x+y
y=x-y
x=x-y
print("After swapping x  : ",x)
print("After swapping y : ",y)

