import random
d={}
while True:
    menu="""
    1. Register
    2. Login
    3. forgot password
    4. Exit
    """
    ch=int(input("Enter your choice: "))
    if ch==1:
        name=input("Enter your name: ")
        mobile=int(input("Enter your mobile number: "))
        email=input("Enter your email: ")
        password=input("Enter your password: ")
        cpassword=input("Enter your confirm password: ")
        
        if password==cpassword:
            print("Registration successful!")
            d['mobile'] = mobile
            d['email'] = email
            d['password'] = password
        else:
            print("Passwords do not match.")
    elif ch==2:
        email=input("Enter your email: ")
        password=input("Enter your password: ")
        if d['email'] == email and d['password'] == password:
            print("Login successful!")
        else:
            print("Invalid email or password.")
    elif ch==3:
        mobile=int(input("Enter your mobile number: "))
        if d['mobile']==mobile:
            otp= random.randint(1000, 9999)
            print(f"Your OTP is: {otp}")
            uotp=int(input("Enter the OTP sent to your mobile: "))
            if uotp == otp:
                new_password=input("Enter your new password: ")
                d['password'] = new_password
                print("Password updated successfully!")
                print(d)
    elif ch==4:
        print(" thank you for using our service. Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")