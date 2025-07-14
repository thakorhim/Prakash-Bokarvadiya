import random

rendome_no= random.randint(1, 50)
while True:
    try:
        user_no = int(input("Enter a number between 1 and 50: "))
        if 1 <= user_no <= 50:
            while True:
                if user_no < rendome_no:
                    print("Your number is too low. Try again.")
                elif user_no > rendome_no:
                    print("Your number is too high. Try again.")
                else:
                    print("Congratulations! You guessed the number!")
                    break
                user_no = int(input("Enter a number between 1 and 50: "))
        else:
            print("Please enter a valid number between 1 and 50.")
    except ValueError:
        print("\033[91mInvalid input. Please enter a number.\033[0m")



