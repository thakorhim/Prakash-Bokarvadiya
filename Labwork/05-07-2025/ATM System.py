user_data={}
total_balance={}
transaction={}

def view_total_balance():
    b=0
    if not total_balance:
        print("No User found.")
        print("Please register a user first.")
        return
    else:
        print("Total balance:")
        for account, balance in total_balance.items():
            print(f"Account {account}: {balance}")
            b=b+balance
        print("Total balance of all accounts:", b)

def view_all_transaction():
    if not transaction:
        print("No transactions found.")
    else:
        print("All transactions:")
        for account, txns in transaction.items():
            print(f"Account {account}:")
            for txn in txns:
                print(f" - {txn}")
    
def  register_new_user():
    while True:
        while True:
            account_number=input("Enter user account Number :")
            if account_number.isdigit():
                print(" User account No :",account_number)
                break
            else:
                print(" Invalide account Number :")
        if account_number in user_data:
           print("Account Number  already exists. Please enter a unique Account  No.")
           continue
    
        while True:           
            name = input("Enter Name: ")
            if not name.isdigit() and len(name) > 2:
                print("Valid name: ", name)
                break
            else:
                print("\033[91mInvalid name. Please enter a valid name containing only letters.\033[0m")
                print("\033[91mName should be more than 3 characters long.\033[0m")
        while True:
            password=input("\033[92mEnter user Password : ")
            cpassword=input(" Enter Conform Password : ")
            print("\033[0m",end="")
            if password==cpassword :
                if  len(password) > 4:
                    print("User  password: ",password )
                    break
                else :
                    print("\033[91mPassword should be more than 5 characters long.\033[0m")
            else:
                print("\033[91mPassword and Conform Password  not match  :\033[0m")
        while True:
            deposit=input("Enter deposit: ")
            if deposit.isdigit():
                print("\033[92mSuccesfuly add ammount :",deposit)
                total_balance[account_number] = total_balance.get(account_number, 0) + int(deposit)
                transaction[account_number]= transaction.get(account_number, []) + [f"Deposited {deposit}"]
                
                print("\033[0m",end="")
                break
            else:
                print("Enter nomber amount : ")
        user_data[account_number]={ 'account_number':account_number,'name': name, 'password': password,'deposit':deposit}
        if account_number in user_data:
            print("\033[92m")
            print("User  Data:")
            print("Account  No:",account_number)
            print("Name:", user_data[account_number]['name'])
            print("Password", user_data[account_number]['password'])
            print("ammount ",user_data[account_number]['deposit'])
            print("Succesfully register user :\033[0m")
            print("\033[0m")
            break

        admin()
def edit_user():
    if not user_data:
        print("No users found.")
        print("Please register a user first.")
        return
    else:
        print("Edit User Information")
    
        while True:
                account_number=input("Enter user account Number :")
                if account_number.isdigit():
                    
                    print("User account No :",account_number)
                    if account_number in user_data:
                        print("User Name:", user_data[account_number]['name'])
                        print("User Password:", user_data[account_number]['password'])
                        while True:
                            name = input("Enter New Name : ")
                            if (len(name) > 2 or name == ""and not name.isdigit()):
                                name = user_data[account_number]['name']
                                break
                            else:
                                print("\033[91mInvalid name. Please enter a valid name containing only letters.\033[0m")
                                print("\033[91mName should be more than 2 characters long.\033[0m")

                        while True:
                            password = input("Enter New Password : ")
                            if len(password) > 3:
                                break
                            else:
                                print("\033[91mPassword should be more than 4 characters long.\033[0m")

                        user_data[account_number]['name'] = name
                        user_data[account_number]['password'] = password

                        print("User information updated successfully.")
                        break
                    else:
                        print("No user found with this account number.")
                        

                    break
                else:
                    print(" Invalide account Number :")
    
       
    
def delete_user():
    if not user_data:
        print("No users found.")
        print("Please register a user first.")
        return
    else:
        print("Delete User Information")
        while True:
            account_number = input("Enter user account Number to delete: ")
            if account_number.isdigit():
                if account_number in user_data:
                    y= input(f"Are you sure you want to delete user with account number {account_number}? (yes/no): ").strip().lower()
                    if y != 'yes':
                        print("User deletion cancelled.")
                        return
                    else:
                        print("Deleting user...")
                        del user_data[account_number]
                        print(f"User with account number {account_number} has been deleted successfully.")
                        break
                else:
                    print("Account Number not found. Please enter a valid Account No.")
            else:
                print("Invalid account Number. Please enter a numeric value.")
def show_all_user():
    if not user_data:
        print("No users found.")
    else:
        print("All registered users:")
        for account_number, user_info in user_data.items():
            print(f"Account Number: {account_number},\nName: {user_info['name']},\nDeposit: {user_info['deposit']},\nPassword: {user_info['password']}\n")


    



def admin():
    manu="""
    ======= Admin Menu =======
    1. View Total Balance
    2. View All Transactions
    3. Register New User
    4. Edit User Info
    5. Delete User
    6. Show All Users
    7. Exit
    ==========================
    """
    
    
    while True:
        print(manu)
        ch=input("enter your choice : ")
        if ch == '1':
            view_total_balance()
        elif ch == '2':
            view_all_transaction()
        elif ch == '3':
            register_new_user()
        elif ch == '4':
            edit_user()
        elif ch == '5':    
            delete_user()    
        elif ch == '6':
            show_all_user()
        elif ch == '7':
            print(" Thnak you ")
            break
        else:
            print(" invalide choice :\n Try again :")


def user():
    while True:
        account_number = input("Enter your account number: ")
        if account_number.isdigit():
            if account_number in user_data:
                password = input("Enter your password: ")
                if password == user_data[account_number]['password']:
                    print(f"Welcome {user_data[account_number]['name']}!")
                    break
                else:
                    print("Incorrect password. Please try again.")
            else:
                print("Account number not found. Please try again.")
        else:
            print("Invalid account number. Please enter a numeric value.")
    
    user_menu = """
    ============= User Menu =============
    1. View Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit
    =====================================
    """
    
    while True:
        print(user_menu)
        choice = input("Enter your choice: ")
        if choice == '1':
            if account_number in total_balance:
                print(f"Your current balance is: {total_balance[account_number]}")
            else:
                print("No balance found for this account.")
          
        elif choice == '2':
            while True:
                deposit = input("Enter amount to deposit: ")
                if deposit.isdigit():
                    deposit=int(deposit)
                    total_balance[account_number]= total_balance.get(account_number, 0) + deposit
                    transaction[account_number] = transaction.get(account_number, []) + [f"Deposited {deposit}"]
                    print(f"Successfully deposited {deposit}. New balance: {total_balance[account_number]}")
                    break
                else:
                    print("Invalid amount. Please enter a numeric value.")
            
        elif choice == '3':
            while True:
                withdraw = input("Enter amount to withdraw: ")
                if withdraw.isdigit():
                    withdraw = int(withdraw)
                    if account_number in total_balance and total_balance[account_number] >= withdraw:
                        total_balance[account_number] -= withdraw
                        transaction[account_number] = transaction.get(account_number, []) + [f"Withdrew {withdraw}"]
                        print(f"Successfully withdrew {withdraw}. New balance: {total_balance[account_number]}")
                        break
                    else:
                        print("Insufficient balance or account not found.")
                        print("Your current balance is:", total_balance.get(account_number, 0))
                        break
                else:
                    print("Invalid amount. Please enter a numeric value.")
        elif choice == '4':
            print("Thank you for using the ATM system!")
            break
        else:
            print("Invalid choice. Please try again.")



menu="""
=====================
Welcome to ATM System
=====================
Login as:
1. Admin
2. User
3. Exit 

"""

while True:
    print(menu)
    ch=input("Enter your choice: ")
    
    if ch == '1':
        admin()
    elif ch == '2':
        user()
    elif ch == '3':
        print("thank you")
        break
    else:
        print("invlide choice :")
        print(" try again :")

print("Exiting the ATM system. Goodbye! user_data")