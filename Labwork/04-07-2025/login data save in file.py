#signup
#login
#forgot password
import random
from datetime import datetime
import re


file=open("user_data.txt", "a")  # Open file to save user data
file.close()  # Close the file after creating it


while True:
    try:    
        d={}
        while True:
            menu="""
            1. Register
            2. Login
            3. forgot password
            4. Exit
            """
            print(menu)
            ch=int(input("Enter your choice: "))
            if ch==1:
                while True:
                    name=input("Enter your name: ")
                    if name.isalpha():
                        break
                    else:
                        print("\033[91mInvalid name. Please enter a valid name.\033[0m")
                while True:
                    try:
                        mobile = int(input("Enter your mobile number (10 digits): "))
                        if len(str(mobile)) == 10:
                            pass
                        else:
                            print("\033[91m Mobile number must be 10 digits.\033[0m")
                            continue
                       

                    except ValueError:
                        print("\033[91m Invalid mobile number. Please enter a valid number.\033[0m")
                        continue
                    else:
                        break
                    
                while True:
                    try:
                        email = input("Enter your email: ").strip()
                        # Simple email pattern
                        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                        if re.match(pattern, email):
                            pass
                        else:
                            print("\033[91m Invalid Email Format\033[0m")
                            continue
                    except ValueError:
                        print("\033[91m Invalid email. Please enter a valid email.\033[0m")
                        continue
                    else:
                        break
                while True:
                    try:
                        password = input("Enter your password : ").strip()
                        cpassword=input("Enter your confirm password: ").strip()
                        if password == cpassword:
                            if len(password) > 3:
                                now = datetime.now()
                                formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
                                file=open("user_data.txt", "a")  # Open file to save user data
                                d['name'] = name
                                d['mobile'] = mobile
                                d['email'] = email
                                d['password'] = password
                                file.write(f"\n\ntime: {formatted_time}\nname: {d['name']}\nMobile: {d['mobile']}\nEmail: {d['email']}\nPassword: {d['password']}\n")
                                file.close()  # Close the file after writing
                            else:
                                print("\033[91m Password must be more than 4 characters.\033[0m")
                                continue
                        else:
                            print("\033[91m Passwords do not match.\033[0m")
                            continue
                    except ValueError:
                        print("\033[91m Invalid password. Please enter a valid password.\033[0m")
                        continue
                    else:
                        break
                print("\033[92m Registration successful!")
                print("\033[0m")
                
                
            elif ch==2:
                if not d:
                    print("\033[91m Please register first.\033[0m")
                    continue
                else:
                    while True:
                        email=input("Enter your email: ")
                        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                            print("\033[91m Invalid Email Format\033[0m")
                            continue
                        password=input("Enter your password: ")
                        if not password:
                            print("\033[91m Password cannot be empty.\033[0m")
                            continue
                        if d['email'] == email and d['password'] == password:
                            print("Login successful!")
                            break
                        else:
                            print("\033[91m Invalid email or password.\033[0m")
            elif ch==3:
                
                while True:
                    try:
                        if not d:
                            print("\033[91m Please register first.\033[0m")
                            break
                        mobile=int(input("Enter your mobile number: "))
                        if d['mobile']==mobile:
                            otp= random.randint(1000, 9999)
                            print(f"Your OTP is: {otp}")
                            uotp=int(input("Enter the OTP sent to your mobile: "))
                            if uotp == otp:
                                while True:
                                    new_password=input("Enter your new password: ")
                                    if len(new_password) > 3:

                                        d['password'] = new_password
                                        print("Password updated successfully!")
                                        print(d)
                                        break
                                    else:
                                        print("\033[91m Password must be more than 3 characters.\033[0m")
                                        continue       
                            else:
                                print("\033[91m Invalid OTP. Please try again.\033[0m")
                        else:
                            print("\033[91m Mobile number not found. Please try again.\033[0m")
                    except:
                        print("\033[91m Invalid input. Please try again.\033[0m")
                        continue
                    else:
                        print("\033[92mPassword reset successful!\033[0m")
                        break
            elif ch==4:
                print("\033[92m Thank you for using our service. Exiting the program.\033[0m")
                break
            else:
                print("\033[91m Invalid choice. Please try again.\033[0m")
    except:
        print("\033[91m Invalid input, please try again.\033[0m")
        continue
    else:
        print("\033[92m Thank you for using our service. Exiting the program.\033[0m")
        break