def l1():
    l=[]
    od=[]
    ev=[]
    for i in range(1, 31):
        if i % 2 == 0:
            ev.append(i)
        else:
            od.append(i)
    print("odd numbers:",od)
    print("even numbers:",ev)

def l2():
    l = [23, 45, 67, 89, 12, 34, 56]
    l.sort()
    print("minimum number in list:", l[0])
    print("largest number in list:", l[-1])
    print("second largest number in list:",l[-2])


def l3():
    n=int(input("enter the number of elements in list: "))
    l = []
    print("press1 : integer")
    print("press2 : string")
    print("press3 : exit")
    ch = int(input("enter your choice: "))
    if ch == 1:
        for i in range(1,n+1):
            x = int(input("enter the number: "))
            l.append(x)
        print("numbers in list:", l)
    elif ch == 2:
            for i in range(1,n+1):
                x = input("enter the string: ")
                l.append(x)
            print("string in list:", l)
    elif ch == 3:
        print("thank you")
        return
    else:
        print("invalid choice")
       

    
       
        
       
    print("list:", l)
        

while True:
    print("press 1: 1 to 30 odd and even numbers")
    print("press 2: largest number in list")
    print("press 3: user defined list")
    print("press 4: exit")
    ch = int(input("enter your choice: "))
    if ch == 1:
        l1()
    elif ch == 2:
        l2()
    elif ch == 3:
        l3()
    elif ch == 4:
        print("thank you")
        break
    else:
        print("invalid choice")