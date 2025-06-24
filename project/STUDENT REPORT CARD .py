# ===============================
#       STUDENT REPORT CARD      
# ===============================

# Enter Student Name: Anjali Mehta
# Enter Roll Number: 23

# Enter marks for 5 subjects:
# Subject 1: 85
# Subject 2: 92
# Subject 3: 78
# Subject 4: 88
# Subject 5: 91

# ----------- Result ------------
# Student Name   : Anjali Mehta
# Roll Number    : 23

# Subject Marks  : [85, 92, 78, 88, 91]
# Total Marks    : 434
# Average Marks  : 86.8
# Percentage     : 86.80%

# Grade          : A

from os import name


def Student_info(name1,roll):
    print("Student Name   : ",name1)
    print("Roll Number    : ",roll)

def Subject_marks(m1,m2,m3,m4,m5):
    sum=m1+m2+m3+m4+m5
    print("Subject Marks  : ",[m1,m2,m3,m4,m5])
    print("Total Marks    : ",sum)
    avg=sum/5
    print("Average Marks  : ",avg)
    per=avg*100/100
    print("Percentage     : ",per)
    return per
def Grade(per):
    if per>=95:
        print("Grade          : A+")
    elif per>=90 and per<95:
        print("Grade          : A")
    elif per>=80 and per<90:
        print("Grade          : B")
    elif per>=70 and per<80:
        print("Grade          : C")
    elif per>=60 and per<70:
        print("Grade          : D")
    else:
        print("fail")

name=input("Enter your name :-")
roll=int(input("Enter your roll no :- "))
m1=int(input("Enter marks for subject 1 :- "))
m2=int(input("Enter marks for subject 2 :- "))
m3=int(input("Enter marks for subject 3 :- "))
m4=int(input("Enter marks for subject 4 :- "))
m5=int(input("Enter marks for subject 5 :- "))
print("----------- Result ------------")
Student_info(name,roll)
Subject_marks(m1,m2,m3,m4,m5)
per=Subject_marks(m1,m2,m3,m4,m5)
Grade(per)
    
