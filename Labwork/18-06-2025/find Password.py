# Hidden password input
real_password = input("Enter the hidden 4-digit password: ")

# Function to check if guessed password is correct
def check(guess):
    return guess == real_password

# Brute-force finder using while True loop
def find_password():
    i = 0
    while True:
        guess = str(i).zfill(4)  # Convert i to 4-digit string
        print("Checking password:", guess)

        if check(guess):
            print("✅ Password Found:", guess)
            break  # Exit the loop

        i += 1  # Try next number

# Run the finder
find_password()

