age=int(input("Enter the age :"))
if age>=18 and age<=35:
    print("Young")  
elif age>=36 and age<=60:
    print("Middle")
elif age>=61 and age<=100:
    print("Old")
else:
    print("Invalid age")    