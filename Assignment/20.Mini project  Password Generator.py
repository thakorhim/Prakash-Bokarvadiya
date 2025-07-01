# 20.Mini project :
# Problem Statement : Password Generator
# Make a program to generate a strong password using the input given by the user.
# To generate a password, randomly take some words from the user input and 
# then include numbers, special characters and capital letters to generate the password.
# Also, keep a check that password length is more than 8 characters. 
# Note: Include Exception handling wherever required. Also, make a ‘User’ class and 
#        store the details like user id, name and password of each user as a tuple


import random
import string

# User class to store user information
class User:
    def __init__(self, user_id, name, password):
        self.details = (user_id, name, password)  # Tuple to store user details

    def display_user(self):
        print("\nUser Created Successfully!")
        print("User ID:", self.details[0])
        print("Name:", self.details[1])
        print("Password:", self.details[2])

# Function to generate password
def generate_password(words_list):
    try:
        if len(words_list) < 2:
            raise ValueError("Enter at least 2 words to generate a strong password.")

        # Randomly select 2 words and capitalize one of them
        word1 = random.choice(words_list)
        word2 = random.choice(words_list).capitalize()

        # Add digits and special characters
        digits = str(random.randint(10, 99))
        special = random.choice("!@#$%^&*()")

        # Combine all parts
        raw_password = word1 + word2 + digits + special

        # Shuffle the characters for more randomness
        password = ''.join(random.sample(raw_password, len(raw_password)))

        # Ensure length > 8
        if len(password) <= 8:
            raise Exception("Generated password is too short. Try using longer words.")

        return password

    except Exception as e:
        print("Error:", e)
        return None

# Main function
def main():
    while True:
        try:
            print("\n--- Password Generator ---")
            user_id = input("Enter user ID (or type 'exit' to quit): ").strip()
            if user_id.lower() == 'exit':
                print("Exiting program.")
                break

            name = input("Enter your name: ").strip()
            input_words = input("Enter a few words separated by space: ").strip().split()

            password = generate_password(input_words)

            if password:
                # Create a User object
                new_user = User(user_id, name, password)
                new_user.display_user()

        except Exception as e:
            print("Unexpected error:", e)


        name = input("Enter your name: ").strip()
        input_words = input("Enter a few words separated by space: ").strip().split()

        password = generate_password(input_words)

        if password:
            # Create a User object
            new_user = User(user_id, name, password)
            new_user.display_user()

        


# Run the program
if __name__ == "__main__":
    main()
