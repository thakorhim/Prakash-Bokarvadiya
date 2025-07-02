def student_data(d):
    while True:
        try:
            s_no = int(input("Enter number of students: "))
            break
        except ValueError:
            print("\033[91m Invalid input. Please enter a numeric  No.\033[0m")
            print("\033[91mPlease try again.\033[0m")

    
    while True:

        if len(d)== s_no:
            print("\033[91m Student data is full. \033[0m")
            break
        while True:
            r = input("Enter Roll No:")

            
            if r.isdigit():
                roll_no = int(r)
                break
            else:
                print("\033[91mInvalid input. Please enter a numeric Roll No.\033[0m")
                print("\033[91mPlease try again.\033[0m")
        

        if roll_no in d:
            print("Roll No already exists. Please enter a unique Roll No.")
            continue
        while True:
            name = input("Enter Name: ")
            if name.isalpha() and len(name) > 2:
                print("Valid name:", name)
                break
            else:
                print("\033[91mInvalid name. Please enter a valid name containing only letters.\033[0m")
                print("\033[91mName should be more than 3 characters long.\033[0m")

        
        while True:
            mobile = input("Enter Mobile Number (10 digits): ")
            if mobile.isdigit() and len(mobile) == 10:
                print("Valid mobile number:", mobile)
                break
            else:
                print("\033[91mInvalid mobile number. Please enter a 10-digit number.\033[0m")

        d[roll_no] = {'name': name, 'mobile': mobile}

        print("\033[92mStudent data added successfully.\033[0m")


def show_student_data(d):        
        if len(d) == 0:
            print("\033[91mNo student data available.\033[0m") 
            return student_data(d)
        else:
            while True:
                while True:
                    roll = input("Enter Roll No to show data: ")
                    if roll.isdigit():
                        roll = int(roll)
                        break
                    else:
                        print("\033[91mInvalid input. Please enter a numeric Roll No.\033[0m")
                        print("\033[91mPlease try again.\033[0m")
                if roll in d:
                    print("\033[92m")
                    print("Student Data:")
                    print("Roll No:", roll)
                    print("Name:", d[roll]['name'])
                    print("Mobile:", d[roll]['mobile'])
                    print("\033[0m")
                    break
                else:
                    print("Roll No not found in the database. Please try again.")
                
                    print("All Roll Nos in the database:")
                    print("-------------------------")
                    for i in d.keys():
                        print("\t", i)
def delete_student_data(d):
    if len(d)== 0:
        print("\033[91mNo student data available to delete.\033[0m")
        return
    while True:
        roll = input("Enter Roll No to delete data: ")
        if roll.isdigit():
            roll = int(roll)
            break
        else:
            print("\033[91mInvalid input. Please enter a numeric Roll No.\033[0m")
            print("\033[91mPlease try again.\033[0m")
    if roll in d:
        del d[roll]
        print("\033[92mStudent data deleted successfully.\033[0m")
    else:
        print("\033[91mRoll No not found in the database. Please try again.\033[0m")


#main
d={}
while True:
    m="""
       1. Add Student Data
       2. Show Student Data
       3. Exit
       """
    print(m)
    choice = input("Enter your choice: ")
    if choice == '1':
        student_data(d)
    elif choice == '2':
        show_student_data(d)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("\033[91mInvalid choice. Please try again.\033[0m")
        