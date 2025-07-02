def student(d):
    dsize=int(input("Enter  students :"))
    print("Enter ",dsize," Data :")
    print("-------------------------")
    for i in range(1,dsize+1):
        name=input("Enter Name :")
        roll=int(input("Enter Roll No :"))
        marks=float(input("Enter Marks :"))
        d[i]={'Name':name,'Roll':roll,'Marks':marks}
        print(i,": student value ")
    print("Student Data :")
    print("      Name      Roll        Marks")
    print("-------------------------------------------")
    for i in d:
        print(*d.values())
d={}
student(d)