user_data={}
total_balance={}
transaction={}

def view_total_balance():
    b=0
    if not total_balance:
        print("No transactions found.")
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
            if name.isalpha() and len(name) > 2:
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
    while True:
            account_number=input("Enter user account Number :")
            if account_number.isdigit():
                print(" User account No :",account_number)
                break
            else:
                print(" Invalide account Number :")
    if account_number in user_data:
        print("User  Data ")
       
    else:
        print("No User found :")




    



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
