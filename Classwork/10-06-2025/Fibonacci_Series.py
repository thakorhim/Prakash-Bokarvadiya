#0 1 1 2 3 5 8 13 21 34 55
n=int(input("enter a number"))
n1=0
n2=1
for i in range(3,n+1):
    
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
# l = []

# for i in range(1,n+1):
#     l.append(n1)
#     n1,n2=n2,n1+n2
# print(l)


